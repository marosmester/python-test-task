#from django.shortcuts import render
from .models import BlogPost
from .serializers import BlogPostSerializer
from myapp import externalAPIs

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def all_blogposts(request, format=None):

    #GET METHOD
    if request.method == 'GET':
        # get all BlogPosts:
        all_blog_posts = BlogPost.objects.all()
        # serialize them:
        serializer = BlogPostSerializer(all_blog_posts, many = True)
        return Response( serializer.data, status=status.HTTP_200_OK)
    
    #POST METHOD
    elif request.method == 'POST':
        serializer = BlogPostSerializer(data=request.data)
        valid_userIDs = externalAPIs.get_all_ids('https://jsonplaceholder.typicode.com/users')
        request_ID = request.data['userid']

        if serializer.is_valid() and (request_ID in valid_userIDs) :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        elif (request_ID not in valid_userIDs):
            return Response(serializer._errors, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def single_blogpost_byID(request, id, format = None):
    
    try:
        blogpost = BlogPost.objects.get(pk=id)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #GET METHOD
    if request.method == 'GET':
        serializer = BlogPostSerializer(blogpost)
        return Response(serializer.data)
    
    #PUT METHOD
    elif request.method == 'PUT':
        serializer = BlogPostSerializer(blogpost, data= request.data)

        if serializer.is_valid() and ( request.data['userid'] == blogpost.userid) :
            serializer.save()
            return Response(serializer.data)
        elif ( request.data['userid'] != blogpost.userid):
            return Response(serializer._errors, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #DELETE METHOD
    elif request.method == 'DELETE':
        blogpost.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
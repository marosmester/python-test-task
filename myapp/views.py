from django.shortcuts import render
from .models import BlogPost
from .serializers import BlogPostSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from myapp import externalAPIs
from myapp import other

@api_view(['GET', 'POST'])
def all_blogposts(request, format=None):

    #GET METHOD
    if request.method == 'GET':
        # get all BlogPosts:
        all_blog_posts = BlogPost.objects.all()
        # serialize them:
        serializer = BlogPostSerializer(all_blog_posts, many = True)
        response = Response( serializer.data, status=status.HTTP_200_OK)
    
    #POST METHOD
    elif request.method == 'POST':
        # Choose a valid ID (in case it wasnt received): 
        received = request.data
        if 'id' not in received.keys():
            received['id'] = other.choose_id()
        
        serializer = BlogPostSerializer(data=received)
        valid_userIDs = externalAPIs.get_all_ids('https://jsonplaceholder.typicode.com/users')
        request_ID = request.data['userId']

        if serializer.is_valid() and (request_ID in valid_userIDs) :
            serializer.save()
            response =  Response(serializer.data, status=status.HTTP_201_CREATED)
        elif (request_ID not in valid_userIDs):
            response = Response(serializer._errors, status=status.HTTP_401_UNAUTHORIZED)
        else:
            response = Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return response
    
@api_view(['GET', 'PUT', 'DELETE'])
def single_blogpost_by_ID(request, id, format = None):
    
    try:
        blogpost = BlogPost.objects.get(pk=id)
        VALID_BLOGPOST = True
    except BlogPost.DoesNotExist:
        VALID_BLOGPOST = False
        response = Response(status=status.HTTP_404_NOT_FOUND)

    #GET METHOD
    if request.method == 'GET':
        if VALID_BLOGPOST:
            serializer = BlogPostSerializer(blogpost)
            response = Response(serializer.data, status=status.HTTP_200_OK)
        else:
            blogpost_dict = externalAPIs.find_post_byID('https://jsonplaceholder.typicode.com/posts', id)
            # if blogpost was found by the 3rd party API:
            if blogpost_dict != None:                                    
                # deserialize it in order to POST it:
                serializer = BlogPostSerializer(data = blogpost_dict)

                # still, return a GET response:
                if serializer.is_valid():
                    serializer.save()
                    response = Response(serializer.data)
    
    #PUT METHOD
    elif VALID_BLOGPOST and request.method == 'PUT':
        serializer = BlogPostSerializer(blogpost, data= request.data)

        if serializer.is_valid() and ( request.data['userId'] == blogpost.userId) and (request.data['id'] == blogpost.id):
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_200_OK)
        elif ( request.data['userId'] != blogpost.userId) or (request.data['id'] != blogpost.id):
            response = Response(serializer._errors, status=status.HTTP_403_FORBIDDEN)
        else:
            response = Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #DELETE METHOD
    elif VALID_BLOGPOST and request.method == 'DELETE':
        blogpost.delete()
        response = Response(status=status.HTTP_204_NO_CONTENT)

    return response

@api_view(['GET'])
def search_blogposts_by_userId(request, userID, format = None):
    blogposts = BlogPost.objects.filter(userId=userID)

    if blogposts.exists():
        serializer = BlogPostSerializer(blogposts, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

# ------------------------------ FRONTEND ------------------------------------
def home(request):
    return render(request, 'index.html', {})

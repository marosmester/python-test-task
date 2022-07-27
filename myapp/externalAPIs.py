import requests
import json

def get_all_ids(endpoint):
    '''
    Iterates over all records at the given endpoint and adds their IDs into a Python set.
    :param endpoint: API url endpoint [str]
    :returns: set containing integers
    '''
    all_users = requests.get(endpoint).json()       # returns a list of JSON records
    userd_ids = set()

    for user in all_users:
        userd_ids.add(user['id'])

    return userd_ids

def find_post_byID(endpoint, id):
    '''
    Searches records at the given endpoint for a record with the desired ID.
    :param endpoint:  API url endpoint [str]
    :param id: post ID [int]
    :returns: a post [dict] or [None] if a post with given ID is not found
    '''
    all_posts = requests.get(endpoint).json()        # returns a list of JSON records
    desired_post = None

    for post in all_posts:
        if post['id'] == id:
            desired_post = post
    
    return desired_post

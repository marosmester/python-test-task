# Python Test Task
This is a one-app project written using Django. This app manages a REST API that enables to communicate with a database in which user-created posts are stored.   

## Overview
API functionalities include:
* viewing posts, selecting by their ID or userID
* editing posts (their 'title' or 'body')
* deleting posts
* creating new posts

The API can be tested using 3rd party services, for example, https://www.postman.com/.
However, whenever you would request the API with something, you can add '.json' at the end of the URL request and a pure JSON output should be displayed in the browser.

## First installation
### Step 1
Create a virtual environment and activate it. After that, some Python packages are required, they can be installed via:
```bash
pip install django
pip install djangorestframework
pip install requests 
```
### Step 2
Start a new Django project and then create one Django app. This can be done by:
```bash
django-admin startproject myproject
cd myproject
python manage.py startapp myapp
```
### Step 3
Provided that the project name and the app name are the same as in this repository, it is sufficient to just copy (and or replace) all the .py files from this repository. Alternatively, some dependencies, such as the app name in 'setting.py' file should be edited. Finally, run the server:
```bash
python manage.py runserver
```

## Full API documentation (Swagger)
https://app.swaggerhub.com/apis/MESTERMAROS/Python_test_task/1.0.0#/

## API URL requests guide (examples)
Using, for instance, https://www.postman.com/ it is possible to: 

GET all posts: \
http://127.0.0.1:8000/blogposts/ \
POST a new post: \
http://127.0.0.1:8000/blogposts/ \
GET/PUT/DELETE a single post with ID=2 : \
http://127.0.0.1:8000/blogposts/id/2 \
GET all the posts with userId=2 : \
http://127.0.0.1:8000/blogposts/userId/2

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
## Step 2
Start a new Django project and then create one Djangoo app. This can be done by:
```bash
django-admin startproject myproject
cd myproject
python manage.py startapp myapp
```

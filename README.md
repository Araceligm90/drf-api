# Project: Django REST Framework and Docker

##### Author: Araceli García


### Links and Resources

Using Django REST framework to create an API, then containerize it with Docker.

### Features

    - Rebuild a custom version of Things API demo 
    - Replace with your own application and model

### Setup

**Initiate a virtual environment**

    - python3.11 -m venv .venv
    - source .venv/bin/activate

**Run this app**

    - docker compose up

**Endpoint to access the url**

    -/api/v1/animals

**To add animals create a user running the below command**

    - docker compose run web python manage.py createsuperuser


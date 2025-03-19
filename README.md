# fastapi-sample-project

## Overview  
This is a FastAPI backend that exposes a secure **GET** endpoint 
- Includes **API key authentication** for security
- Implements **unit testing** based on **HTTPX** and can be used directly with FastAPI 

Tutorial link

https://fastapi.tiangolo.com/tutorial/testing/#extended-testing-file

https://jnikenoueba.medium.com/unit-and-integration-testing-with-fastapi-e30797242cd7

## Setup & Installation
```sh
   git clone https://github.com/cynthia-natalie/fastapi-sample-project.git
   cd fastapi-sample-project
   pip install -r requirements.txt
   
   run fastapi app:
    uvicorn app.main:app

   post an item:
    curl -X 'POST' 'http://127.0.0.1:8000/items/' -H 'accept: application/json' -H 'x-token: coneofsilence' -H 'Content-Type: application/json' -d '{"id": "foo", "title": "Foo", "description": "There goes my hero"}'

   get an item:
    curl -X 'GET' 'http://127.0.0.1:8000/items/foo' -H 'accept: application/json' -H 'x-token: coneofsilence'

   run unit tests:
    pytest
   ```

## Video Demo

Video Demo Link: https://drive.google.com/file/d/138nn66obP0KkEr1hSsU89oliUnHTOGqj/view?usp=drive_link
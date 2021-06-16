# RocketDataProject

REST API for directory of employees application with DRF. Deploying to docker with docker-compose.

# Run the app

Application is deployed to docker, `Dockerfile` for the DRF app and `docker-compose.yaml` files are configured using PostgreSQL database to run the app using docker

#### Run docker containers
###### Build all the containers
    docker-compose up --build

#### DB seeder is used to automatically fill the database
###### Run DB seeder

In a `new terminal`, write the following commands:
    
    docker-compose exec web bash

    python3 management/commands/seed.py

## Get token to authenticate user

### Request
`POST api/token/`

    {
      "username": "sample",
      "password": "sample"
    }
    
### Response
    {
      "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxNTg4NjIxMywianRpIjoiYmQzNDY2ODBjMzQ4NGM4MDlkYzU5MTEyNGMyYTcyOGUiLCJ1c2VyX2lkIjoxfQ.unKxo3IUbmVzFDvkvcPKoSrqpgv1JAvdRAiLExDF0d8",
      "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE0NTAzODEzLCJqdGkiOiI5MTVkYzY4MWExMjM0Y2E1YjMwYzE4NmNkZjc2NTVjMCIsInVzZXJfaWQiOjF9.Sxv8jU-Q685FMuAiPJisa9Nxnp3-B4MmWSmLary9O_M"
    }
    
#### Add Bearer token to request headers to be authenticated

    Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE0NTAzODEzLCJqdGkiOiI5MTVkYzY4MWExMjM0Y2E1YjMwYzE4NmNkZjc2NTVjMCIsInVzZXJfaWQiOjF9.Sxv8jU-Q685FMuAiPJisa9Nxnp3-B4MmWSmLary9O_M

## Get info about employees 
    
###### Information for yourself
    GET /api/employee/
###### Information for yourself at a specific level
    GET /api/employee/?level=1
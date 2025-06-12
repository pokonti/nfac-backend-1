# Nfac homework

## Features

- FastAPI-based REST API
- PostgreSQL database
- Docker & Docker Compose 
- GitHub Actions CI/CD (not sure how it works)
- JWT-based authentication
- Project CRUD


## Docker Hub
```
docker pull antay/nfac-backend:latest
```


## CI/CD

This repo uses GitHub Actions to:
* Build the Docker image
* Push to Docker Hub on every push to main

Secrets needed in GitHub:
* DOCKER_USERNAME
* DOCKER_PASSWORD

## System design

[link](https://drive.google.com/file/d/1cPQ_ePRuy_P37neIYTDx-c6JSCebux5w/view?usp=sharing)
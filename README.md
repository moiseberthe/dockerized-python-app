# Docker project with Streamlit, FastAPI and MongoDB

This project is a demonstration of using Docker Compose to run a `Python` application consisting of `Streamlit`, `FastAPI`, and `MongoDB` in `Docker` containers.<br>
<p align="center">
  <!-- <img align="center" alt="Gif" width="500" src="https://github.com/moiseberthe/m2sise-mlops/assets/75121872/77cc1f84-0629-4cbd-87a4-47edc98451e7"> -->
</p>
<p align="center">
  <img align="center" alt="Gif" width="500" src="https://github.com/moiseberthe/m2sise-mlops/assets/75121872/fc90e9fc-63d7-400e-bbea-ee5a8364b7cf">
</p>

## Prerequisites

Make sure you have `Docker` and `Docker Compose` installed on your machine.

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Clone project

```bash
git clone https://github.com/moiseberthe/dockerized-python-app.git
```

## Project structure

- `client/`: Application Streamlit
- `server/`: Application FastAPI
- `utils/`: train models for `iris` and `penguins` classification

## Docker setup
The Docker files (`client/Dockerfile` and `server/Dockerfile`) contain the build configurations for the Streamlit and FastAPI services.<br>

The `docker-compose.yml` file contains the Docker configuration for the services.

### Build and run containers

```bash
docker compose up --build
```

The project will be accessible at the following address:

- Streamlit: [http://localhost:8501](http://localhost:8501)
- FastAPI: [http://localhost:8000](http://localhost:8000)

## App setup

Make sure to adjust the application files (`client/app.py` and `server/app.py`) according to your needs.

<!-- ## Other commands

Remove all unused images, not just dangling ones.

```bash
docker image prune -a
```

Push a Docker image to the GitHub Container Registry.

```bash
docker push ghcr.io/moiseberthe/mlops:latest
``` -->

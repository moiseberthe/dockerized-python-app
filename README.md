# m2sise-mlops

# Docker project with Streamlit, FastAPI and MongoDB

This project is a demonstration of using Docker Compose to run a `Python` application consisting of `Streamlit`, `FastAPI`, and `MongoDB` in `Docker` containers.
<p align="center">
  <img align="center" alt="Gif" width="500" src="https://github.com/moiseberthe/m2sise-mlops/assets/75121872/77cc1f84-0629-4cbd-87a4-47edc98451e7">
</p>

## Prerequisites

Make sure you have `Docker` and `Docker Compose` installed on your machine.

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Project structure

- `client/`: Application Streamlit
- `server/`: Application FastAPI
- `utils/`: Classification `iris` et `Penguins`

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

## Other commands

Remove all unused images, not just dangling ones.

```bash
docker image prune -a
```

Push a Docker image to the GitHub Container Registry.

```bash
docker push ghcr.io/moiseberthe/mlops:latest
```

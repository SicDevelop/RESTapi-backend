## Requirements
  - Docker compose
  - Poetry

## Installation

U can use WSL linux for start backend service and use windows with docker.

### Linux:
```sh
user@device#: git clone https://github.com/SicDevelop/RESTapi-backend.git
user@device#: cd RESTapi-backend
user@device#: poetry install
user@device#: docker compose --env-file .env up -d
user@device#: make dev
```

Tested on:
```sh
MacOS Big Sur 11.7.4
```

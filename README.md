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

## PgAdmin:
After running the `docker compose` command, You will also get pgAdmin (web interface to the database) running. If you have worked with it before, this is a big plus. 
The configuration data for the connection is in the `.env` file and you can customize it. To connect pgAdmin to PostgresSQL, use the db address, because the docker works like this

Tested on:
```sh
MacOS Big Sur 11.7.4
```

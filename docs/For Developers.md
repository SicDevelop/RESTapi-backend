# Kingdom for developers.

Вы можете поднять API вне докера.

## Requirements:
- poetry
- docker

Для запуска:
```sh
user@device#: git clone https://github.com/SicDevelop/RESTapi-backend.git
user@device#: cd RESTapi-backend
user@device#: poetry install
user@device#: docker compose --env-file .env up -d
user@device#: make export_env
user@device#: make startdev
```


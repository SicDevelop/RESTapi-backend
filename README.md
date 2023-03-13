<div align='center'>
  <image src='https://github.com/SicDevelop/RESTapi-backend/blob/main/docs/images/banner.png' height=500/>
  <h1>Kingdom system</h1>
  <img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/SicDevelop/Kingdom-System?style=plastic">
  <img alt="GitHub issues" src="https://img.shields.io/github/issues/SicDevelop/Kingdom-System?label=Issues">
  <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/SicDevelop/Kingdom-System">
</div>

## Requirements
  - Docker compose (or simply docker)
  - Poetry (for developer branch)

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
### In docker:
```sh
user@device#: git clone https://github.com/SicDevelop/RESTapi-backend.git
user@device#: cd RESTapi-backend
user@device#: docker compose --env-file .env up
```

Для более подробного гайда используйте [wiki](https://github.com/SicDevelop/Kingdom-System/wiki)
Tested on:
```sh
MacOS Big Sur 11.7.4
```

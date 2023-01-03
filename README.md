# Бекэнд часть для расписания для Салаватского Индустриального Колледжа

### Использование

```bash
user@macos#: cd src
user@macos#: make run
```

Инструмент `make` сам установит все необходимые зависимости и запустит докер контейнеры.

### Запросы

##### Для Администратора:

`/api/admin/register` - Для создания учетной записи;

`/api/admin/login` - Для получения JWT токенов;

`/api/admin/view` - Тестовый запрос;

`/api/admin/refresh_token` - для рефреша токена используя _refresh_token;_

`/api/admin/new_teacher` - для добавления нового преподавателя;

`/api/admin/new_group` - для добавления новой группы;

`/api/admin/new_shedule` - для добавления расписания;

##### Публичные:

`/api/public/teacher` - получение json объекта преподавателей

`/api/public/groups` - получение json объекта групп

`/api/public/get_shedule` - получение расписания по названию(?) группы (сейчас не работает)

[Swagger](https://app.swaggerhub.com/apis/blcklptn/fast-api/0.1.0)

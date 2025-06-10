# Dogygram
Это API-приложение по добавлению собак и пород

## Стек технологий

![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?logo=postgresql&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?logo=nginx&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)


## Установка

### Клонирование репозитория

```bash
git clone https://github.com/WarfoIomey/Dogygram.git
cd Dogygram
```

## Структура проекта

- `backend/` — содержит исходный код серверной части приложения.
- `dogygram/` — основное приложение Django.
- `dogs/` — приложение для работы с собаками и пародами.
- `api/` — реализация API на основе Django REST Framework.

## API документация

Основные эндпоинты:

- `GET /api/dogs/` — получение списка собак.
- `POST /api/dogs/` — создание новой собаки.
  - Пример добавления собаки:
  ```
    {
        "name": "Бобик>",
        "age": 10,
        "gender": "Самец",
        "color": "черный",
        "favorite_food": "Мясо",
        "favorite_toy": "Мячик",
        "breed": 1,
        "avg_breed_age": 4.0
    }
  ```
- `GET /api/breeds/` — получение списка пород.
- `POST /api/breeds/` — создание новой породы.
  - Пример добавления породы:
  ```
    {
        "name": "Чихуа",
        "size": "Small",
        "friendliness": 1,
        "trainability": 1,
        "shedding_amount": 2,
        "exercise_needs": 5
    }
  ```

## Развёртывание на сервер

Выполните следующие команды:
```bash
docker compose up
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py collectstatic
docker compose exec backend cp -r /app/collected_static/. /backend_static/static/
```
Для создания суперпользователя выполните следующую команду:
```bash
    docker compose exec backend python manage.py createsuperuser
```

После успешного выполнения этих команд приложение будет доступно по адресу <http://127.0.0.1:8000/>.

## Настройки окружения

Перед запуском приложения настройте переменные окружения (пример в файле .env_example):

- `POSTGRES_USER`— пользователь базы данных.
- `POSTGRES_PASSWORD`— пароль пользователя базы данных.
- `POSTGRES_DB`— имя базы данных PostgreSQL.
- `SECRET_KEY` — секретный ключ Django.
- `DB_HOST` — хост базы данных.
- `DB_PORT` — порт для подключения к базе данных.
- `ALLOWED_HOSTS` — список доступных хостов.
- `DEBUG` — статус отладки Django.
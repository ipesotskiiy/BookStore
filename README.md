# Bookstore
Данный проект предсталяет собой книжный магазин с авторизацией по jwt-токенам, фильтрацией по жанрам, комментирования товара, добавления товара в избранное, а так же показ рекомендуемый товар.
Написан этот проект был для уже существующего фронтенда https://github.com/Ireal-ai/bookstore-react

 # Используемые языки и фреймворки 
 - Python 3.10
 - Django 4.2.2
 - Django Rest Framework 3.14.0

# Используемые базы данных
- PostgreSQL 2.9.3

# Запуск проекта
Сделать клон проектов
git clone https://github.com/ipesotskiiy/bookstore-react
git clone https://github.com/ipesotskiiy/bookstore

После чего необходимо установить библиотеки pip install -r requirements.txt

Создать .env файл в котором будут указаны данные для бд

Создать дирректорию log и файл log.log

![image](https://github.com/ipesotskiiy/bookstore/assets/82309024/3cb41eaa-33be-4980-a9bb-e294cb2cfc2d)

Сделать миграции ```python manage.py migrate```

# Для локального запуска
```
python manage.py runserver
```

# Функции API
- http://127.0.0.1:8000/swagger - получение свагера

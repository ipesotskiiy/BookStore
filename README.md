# bookstore
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

# Функции API
- http://127.0.0.1:8000/swagger - получение свагера
- http://127.0.0.1:8000/book/all - получение всех книг
- http://127.0.0.1:8000/book/add-comment - добивать комментарий
- http://127.0.0.1:8000/book/rate - добавить рейтинг
- http://127.0.0.1:8000/book/recommendations&exclude=<id> - получить рекомендации
- http://127.0.0.1:8000/book/genres - получить жанры
- http://127.0.0.1:8000/book/genres/<id> - получить конкретный жанр
- http://127.0.0.1:8000/book/favorites - получить избранное
- http://127.0.0.1:8000/book/favorites/<id> - получить книгу из избраного
- http://127.0.0.1:8000/book/add-favorites/<id> - добавить книу в избранное
- http://127.0.0.1:8000/book/<id> - полчить конретную книгу
- http://127.0.0.1:8000/auth/signup - зарегистрировать пользователя
- http://127.0.0.1:8000/auth/signin - войти 
- http://127.0.0.1:8000/auth/user/upload-avatar - обновить аватар
- http://127.0.0.1:8000/auth/user/<pk> - обновить профиль

После чего необходимо установить библиотеки pip install -r requirements.txt

Создать .env файл в котором будут указаны данные для бд

Создать дирректорию log и файл log.log

![image](https://github.com/ipesotskiiy/bookstore/assets/82309024/3cb41eaa-33be-4980-a9bb-e294cb2cfc2d)

Сделать миграции ```python manage.py migrate```

# Для локального запуска
```
python manage.py runserver
```
**Модели в приложении пользователя**

Модель пользователя

![image](https://github.com/Ireal-ai/bookstore/assets/82309024/563f1454-2abf-44f6-9668-0cd8f4660a35)

**Менеджеры в приложении пользователя**

Менеджер для создания пользователя

![image](https://github.com/Ireal-ai/bookstore/assets/82309024/b8dd4d46-33ab-4602-9e8e-18b12d572ff8)

**Сериализаторы приложения пользователя**

Сериализатор пользователя

![image](https://github.com/Ireal-ai/bookstore/assets/82309024/86574d1c-89e8-4022-ade1-694b917a1301)

Сериализатор для загрузки аватара

![image](https://github.com/Ireal-ai/bookstore/assets/82309024/8f6a7413-635a-4204-a018-a518a468f8c9)

Сериализатор регитрации с проверкой адреса электронной почты на уникальность, а так же на идентичность вводимых паролей

![image](https://github.com/Ireal-ai/bookstore/assets/82309024/f24c978e-6d66-4eda-aa58-c315db20e4c3)

![image](https://github.com/Ireal-ai/bookstore/assets/82309024/38335f2c-b6cc-4310-8a0e-af80078a0079)

Сериализатор входа

![image](https://github.com/Ireal-ai/bookstore/assets/82309024/a1894c4a-15d2-410c-b008-1c250c54c31e)

**Views приложения пользователя**

Регистрации

![image](https://github.com/Ireal-ai/bookstore/assets/82309024/3a264bf2-da66-4879-87f6-85724d527c39)

Входа

![image](https://github.com/Ireal-ai/bookstore/assets/82309024/aebbe949-a7db-4af9-8f17-959076ee8f2e)

Создания профиля

![image](https://github.com/Ireal-ai/bookstore/assets/82309024/de9f480b-4a0b-47e2-b75c-223f2576f5bc)

Обновления профиля

![image](https://github.com/Ireal-ai/bookstore/assets/82309024/06be277f-9600-46f1-b396-ec9706aec9b0)

Загрузка аватара

![image](https://github.com/Ireal-ai/bookstore/assets/82309024/286b0b50-92ac-411c-a5ed-7dae38314e55)

**Модели приложения продукта**

Модели жанров и книг

![image](https://github.com/Ireal-ai/bookstore/assets/82309024/54ec672a-725a-4a24-8b16-982f02331bc6)

Модели комментариев и рейтинга

![image](https://github.com/Ireal-ai/bookstore/assets/82309024/5cebe051-481b-4495-9569-50979db7395e)

**Фильтры приложения продукта**

Фильтр по жанрам и цене

![image](https://github.com/Ireal-ai/bookstore/assets/82309024/2ada1365-7cce-4bd2-aeed-c10518010d44)

**Сериализаторы приложения продукта**

Сериализатор комментариев

![image](https://github.com/Ireal-ai/bookstore/assets/82309024/3e9bf353-48ae-4514-8859-71df78eab642)

Сериализаторы жанров и рейтингов

![image](https://github.com/Ireal-ai/bookstore/assets/82309024/b749e83f-49c8-4e31-bfa7-97c47ac2d676)

Сериализатор книги с функцией асчёта среднего рейтинга

![image](https://github.com/Ireal-ai/bookstore/assets/82309024/d4bcbcb9-e146-4a72-81fb-702632dce273)

Сериализатор избранного

![image](https://github.com/Ireal-ai/bookstore/assets/82309024/46817580-c6f9-45e8-9e67-f4ac13b50ef6)

**Views приложения продукта**

Выдачи всех жанров, создания рейтинга, выдачи одной книги

![image](https://github.com/Ireal-ai/bookstore/assets/82309024/6ebdcee4-9419-408c-a7e8-ab92e4f6b9ec)

Выдачи нескольких книг

![image](https://github.com/Ireal-ai/bookstore/assets/82309024/5e673c56-bd08-4e98-9ff9-ef15a6289b5c)

Создания комментария, выдачи рекомендаций

![image](https://github.com/Ireal-ai/bookstore/assets/82309024/07a8dccb-7912-417c-8aa9-211ed145f356)

Выдачи, добавления и удаления избранного

![image](https://github.com/Ireal-ai/bookstore/assets/82309024/3c85bb47-ce21-4dab-ae6c-76923e4373f9)

**Настройки свагера**

![image](https://github.com/Ireal-ai/bookstore/assets/82309024/be1e01bc-f9e2-47ad-86c8-e9031c460c87)


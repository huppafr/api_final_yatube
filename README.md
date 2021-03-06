# API-YaTube

Проект был создан для изучения Django REST Framework.
Сервис полволяет получать выборку из базы данных в формате JSON из проекта YaTube и проводить все манипуляции с данным.

# Технологии

- Python 3.9
- Django 3.0.5

# Установка

1. Клонируйте репозиторий на локальный компьютер
2. Создайте и активируйте виртуальное окружение
```bash
python3 -m venv venv
. venv/bin/activate
```
3. Установите зависимости
```bash
pip install -r requirements.txt
```
4. Выполните миграции
```bash
python manage.py makemigrations
python manage.py migrate
```
5. Создайте администратора
```bash
python manage.py createsuperuser
```
6. Запустите проект локально
```bash
python manage.py runserver
```
Готово, проект доступен по адресу http://127.0.0.1:8000/

# Тестовый контент
## Пример
На странице  http://127.0.0.1:8000/admin/posts/

## Автор

- Хюппенен Артем

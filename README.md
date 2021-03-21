# Online Store
## Учебный проект онлайн магазина (не боевой) [из курса](https://djangochannel.com/course/programming/development-of-an-online-store-on-django/)

### Установка

#### 1) 
    переименовать файл Store/local_settings_dev.py в local_settings.py
    прописать свое подключение к БД в local_settings.py
  
#### 2) Создать виртуальное окружение

    python -m venv venv

#### 3) Активировать виртуальное окружение
   
#### 4) Устанавливить зависимости:
    pip install -r req.txt

#### 5) Выполнить команду для выполнения миграций
    python manage.py migrate

#### 6) Создать суперпользователя
    python manage.py createsuperuser

#### 7) Запустить сервер
    python manage.py runserver

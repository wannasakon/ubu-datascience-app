# ubu-datascience-webapp

```sh
python -m pip install pipenv --user
pipenv install django
pipenv shell
django-admin startproject webapp
cd webapp
python manage.py startapp myapp
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

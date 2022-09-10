# Django Learning Repository 📖️

## Setup

- Create your virtual environment:
```bash
virtualenv <ENV_NAME>
```
- Then activate your virtual environment by (in my case that is setting env in Ubuntu):
```bash
cd env/bin/
source activate
```
**Vitrual env is always deactivating when you turn off your computer,
so you need to repeat the process everytime you watch the computer.**

- Starting a project:
```bash
django-admin startproject <PROJECT_NAME>
```

## Running server
```bash
python3 manage.py runserver
```

## Migrate
```bash
python3 manage.py migrate
```
The **migrate** command looks at the **INSTALLED_APPS** setting and creates
any necessary database tables according to the database settings in your
<PROJECT_NAME>/settings.py

## Creating models
```python
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```
- Each field is represented by an instance of a **Field** class - e.g., **CharField** for
character fields and **DataTimeField** for datetimes.

## Activating models
- To include app in your project, we need to add a reference to INSTALLED_APPS setting.
```python
# <PROJECT_NAME>/ settings.py

INSTALLED_APPS = [
    '<APP_NAME>.apps.<APP_NAME>Config',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
Now Django knows to include the <APP_NAME>

- Run:
```bash
python3 manage.py makemigrations <APP_NAME>
```
By running makemigrations, you’re telling Django that you’ve made some changes to your models.

- Command that will run the migrations for you and manage your database schema automatically.
```bash
python3 manage.py sqlmigrate <APP_NAME> 0001
```

- Create those model tables in your database:
```bash
python3 manage.py migrate
```

# Three-step guide to making model changes:
- Change your models (in models.py).
- Run **python manage.py makemigrations** to create migrations for those changes.
- Run **python manage.py migrate** to apply those changes to the database.

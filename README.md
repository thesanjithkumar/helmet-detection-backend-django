# HELMET DETECTION BACKEND

## Check the settings.py file once for correct DB settings and change it accordingly

```Bash
git clone https://github.com/thesanjithkumar/helmet-detection-backend-django.git
```

```Bash
cd helmet-detection-backend-django
```

```Bash
pip install virtualenv
```

```Bash
virtualenv django_env
```

## Activate the virtualenv "django_env"

```Bash
pip install -r requirment.txt
```

```Bash
python manage.py makemigrations
```

```Bash
python manage.py migrate
```

```Bash
python manage.py runserver
```

## Go to http://localhost:8000 to see the output

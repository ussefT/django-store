## Django

- [Django-cms](https://www.django-cms.org)
- [Wagtial](https://wagtail.org)
- [mange.py]()
- [setting.py]()
- [database]()
- [architecture]()
- [MiddleWare]()
- [ORM]()
- [cach]()
- [templates]()

For install django in linux, create virtualenv
```python
python3 -m virtualenv env
```
Install module
```python
pip install -r requirement.txt
```

After that create app 

```python
django-admin startproject store
```

run app

```python
python3 manage.py runserver 0.0.0.0:3000 
```

#### app

In django detail can use microapp. We can use another in the main app
can install like module. Like isbn

```python
manage.py startapp nameApp
```

installation on the main:
- App
- Define model
- Url
- View

---
### setting.py



---
### mange.py

We can use this app for contorl own django like: migrations data base, runServer

Open shell can create model and get models on the database

```python
./manage.py shell
```
on the shell get all data with manager 

```python
p=Product.objects.all()
```

sorts 
```python
p.order_by('name')
```

know django what query 
```python
print(p.query)
```
query
read this [query]()
```python
# exactly 
Product.objects.filter(price__exact=120000)

# less than
Product.objects.filter(price__lt=120000)

# greater than
Product.objects.filter(price__gt=120000)

# start with
Product.objects.filter(price__range=(500,12000))

# two filter and 
Product.objects.filter(price__gt=300,price__lt=1000)

sp=Product.objects.filter(price__exact=120000)
sp.filter(price__lt=300)

```

complecated query with this

```python
from django.db.models import Q

q=Q(price__lt=100)

q1=Q(price__gt=2000)

# and query
q=q1 & q

# or query
q=q1 | q

p=Product.objects.filter(q)

```

raw query
```python
Product.objects.raw("SELECT ... ")
```

---
### architecture

In php, we are write any code on file php, html, css this good for starter.

Model MVC:
    > Model -> Database (second comminucation with database)
    > View -> UI (third set ui ) 
    > Controler -> Logic (first request on this run on logic )
    > (fourth send respose)

In django use MVT:
    > Model -> Database
    > View -> Logic
    > Template -> UI

Image django do work
![work Django]()

---
### MiddleWare

Work start and end request for security, clean request, normalize request, stop or redirect request.
DOS (Denial of service)


---
### ORM
 

    - connection
    - query
    - object

When we are two version of app and update version 1 to version 2, we are use DB versioning and migration.
We can change version with migrations.

show all database and detail
```python
python3 manage.py showmigrations
```

run one app and one code a database
```python
python3 maange.py migrate app 002
```

or migrate all 
```python3
python3 mange.py migrate
```

In migrations create new version database base old version update to new database

```python

```
When use relation btw models first migrate 
When makemigrations and create file migrate000x in folder migrate can remove before migrate

If remove migrate 
```python
./manage.py migrate zero
```

### id

In Django automatic add Id column in to database auto increament


## cache

When a user request page, we are save cach in redis in ram.

## database

- SQL

    SQLite -> onyl use for one user
    Oracle -> best for multi users can buy it
    PostgreSQL -> best for multi users (open users)
    Mysql/Mariadb -> Mariadb is open source MySQL

- NoSQL

collection (mongodb,elasticsearch)
key-value (redis) -> cache
timeseries (influxdb)
widecolumn (cassandra)
graph (neo4j)


---
## templates
Two engine can render html in python
Django Temeplate Engine (DTE)
Jinja

Escape [html entities] :
in html can write special word browser can understand
& gt -> >  [EntityHTML](https://www.w3schools.com/html/html_entities.asp)

If use editor in site we dont use 
[TextEditor](https://www.tiny.cloud/docs/tinymce/latest/basic-example/)

```html
{% autoescape off%}
....
{% autoescape%}
```
- [static]()
- [block]()
- [for]()
- [if]()
- [debug]()
- [include]()
Dajango can render HTML page for that recognise file :

```bash

```

### for

```html
{% for i in item %}
{{item.name}}

{% empty %}
<p> is empty </p>
{% endfor %}
```

### static
In app folder (templates) in templates put (static) 

for load static file 

STATIC_URL in setting that folder use in STATIC_URL/appname/js

```html
{%load static%}
...
<script src="{% static 'appname/js/holder.min.js' %}"</script>
```

### block
Django can render html inner html with block
In setting.py 
```python
        # scan additionl dir
        'DIRS': [BASE_DIR / 'templates'],
        # scan dirs in apps 
        'APP_DIRS': True,
```
base.html
```html
{% block name%}
No Content
{% encblock %}
```

product.html
```html
{% extends 'base.html'%}
...

{% block name%}

{% endblock %}
```

#### deug 
you in template debug var with and break point in pycharm pro.
```html
{% debug %}
```


#### include
This tag can render section in html like header, footer
```html
{% include 'bits/main_header.html' %}
```



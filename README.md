## Django

- [Django-cms](https://www.django-cms.org)
- [Wagtial](https://wagtail.org)
- [mange.py]()
- [setting.py]()
- [MiddleWare]()
- [database]()
- [architecture]()
- [ORM]()
- [cach]()
- [form]()
- [templates]()
- [auth]()
- [authentication]()
- [authorization]()
- [accounting]()
- [url]()
    > [url](https://docs.djangoproject.com/en/5.2/ref/urls/)
- [csrf]()
- [enctype]()
- [SMTP]()

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
## form
Form like model but show in HTML
Form:
    filed: type, widget, validator
3 way can validate field
- [form in template]()
- [custome form]()
- [default form]()
- [user auth form]()
- [validatore]()
- [clean_name]()
- [use-another-library]()


Two models Form 
- forms.Form
> customs form 
- forms.ModelForm
> generate form on own Model

### validatore


### clean_name
For use this clean_(name field)
```python
def clean_name(self):
        if self.cleaned_data['name']==self.cleaned_data['password1']:
            raise ValidationError('Name is not same password')
        return self.cleaned_data['name']
```

### costume form
Define form manually
```python

class SignupForm(forms.Form):
    name=forms.CharField(label='name',max_length=100)
    family=forms.CharField(label='family',max_length=100)
    email=forms.EmailField()
    password1=forms.CharField(label='password',max_length=100,widget=forms.PasswordInput())
    password2=forms.CharField(label='password',max_length=100,widget=forms.PasswordInput())
    phone=forms.CharField(label='phone',max_length=100,validators=[validators.RegexValidator(r'(\+98|09|9)?9\d{8}$')
                                                                   ,validators.MinLengthValidator(5),
                                                                   validators.MaxLengthValidator(20)])
    # phone=PhoneNumber()

    # if validatore for form is not exist this a way
    def clean_name(self):
        if self.data['name']==self.data['password1']:
            raise ValidationError('Name is not same password')
        return self.data['name']

```


### default form
Use this way, pickup from own model
```python
from django import forms
class SignupFomr(forms.ModelForm):
    class Meta:
        model=models.User
        fields=['first_name','last_name','email','phone']
        # fields="__all__" # show all fields
        exclude=['is_superuser','is_staff','is_active'] # not active

```


### user auth form
Use model in django that use in user auth

```python
from django.contrib.auth.forms import UserCreationForm

# use model default django user auth
class SignUpForm(UserCreationForm):
    class Meta:
        model=models.User
        exclude=['is_superuser','user_permissions'
            ,'last_login','date_joined','avatar'
                 'groups','is_staff','is_active'] # not active
```
### form in template


Use split form 
every form:
- form.first_name
- form.first_name.label_tag
- form.first_name.error

For none field error 
```html
        {{ form.non_field_errors }}
```

send from view GET
```html
 <tr>
            <td>{{form.first_name.label_tag}}:</td> <td>{{ form.first_name }}</td>
</tr>
```

We can use for
```html
   <table>
       {% for field in form %}
           <tr>
           <td> {{ field.errors }}</td>
           </tr>
           <tr>
           <td> {{ field.label_tag }} : {{ field }} {% if field.help_text %} {{ field.help_text }}{% endif %}</td>
           </tr>

       {% endfor %}
   </table>
```
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
---
## auth
- Basic Auth
stateless no memory, like alert in browser
Add header (Authorization : Basic [base64] ) use for router and modemADSL
- Session Auth
> Best for browser
- Token Auth
> Generate a code, send for user after that every time user req send this
- JWT
> Json Web Token 1- acceses token 2- refresh token for access token send refresh token for app
- OAuth
> Open Auth, login with Google,github
- External (SSO)
> Library or another way.Single Sign up. like KEYCLOACK

Django use Session Auth.

---
## authentication

swappable means can change class in djano

If use auth field use this import
> from django.contrib.auth.models import AbstractBaseUser


If use auth in base import 
> from django.contrib.auth.models import AbstractUser

0

use own auth dynamic use in models
```python
# this import tell django use model auth that in setting define and dynamic
# after if change account app this model is not crash

from django.contrib.auth import get_user_model
```


---
## authorization

---
## accounting

---

## url
In djnago can use this:
```text
use path -> /store/product/<pid>
use re_path -> /store/product/(?P<pid>\d+)
```

### login

Default django does define login in url auth but does not have 
html we can create HTML login in own auth this example account

## crsf
Defend from XSRF, XSS

## enctype
- text/plain 
> Data is raw send to server
- application/x-www-form-urldecoded
> Encoded url 
- multipart/form-data
> Best for upload file

## SMTP
First protocl for transfer, recive, send Mail.
- Recieve work with POP3,IMAP (MDA = Mail Delivery Agent) (Best app for this Dovecoat) 
- Send work with SMTP (MTA = Mail Transfer Agent) (Best app for this Postfix)
Gmail, Yahoo like post

- SMTP is PORTS
> 25 -> Server to Server
> 465
> 587
> 2525 

For encrypted mail use STARTLS,TLS 

If use this install postfix but we can not find spam.

For use gmail send email
```bash
dig +short gmail.com mx 
# some number is low better
```
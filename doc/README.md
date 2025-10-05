### Store

 - [Admin]()
 - [Product]()
 - [Add Product]()
 - [auth]()

Admin page

```url
http://127.0.0.1:8000/admin
```


## auth
If custome auth in django you must create another app and change setting in setting.py 

[account]()

0
Important if this change database is error with makemigration remove or delete
and change models import (can delete database when makemigration create new)

0
Remember before makemigrations core mkaemigrations account 

```python
# set auth user instead default auth django
AUTH_USER_MODEL = 'account.User'
```

### login
By default django does not have HTML for login, only define in url,
in account define template HTML login 
### Graphql project
 in this project I am working on Graphql with django. Firstly I have created a django project as I normally do.<br>

 To work Graphql with django you need a package called "Graphene-Django". <br>
 
Installation
 ```
 pip install graphene-django
 ```
Then added it to settings.py file
``` python
INSTALLED_APPS = [
    ...,
    'graphene_django',
]
```

# create schema for graphql
create a schema.py into django app

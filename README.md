# SIMPLE-CRUD-WITH-RESTFRAMEWORK
C.R.U.D avec Django Rest Framework

Voici une procédure pour créer une API avec 	Django Rest Framework

## 1. Création du projet Django
`django-admin startproject pollsapi`

## 2. Création de la base de données
`python manage.py migrate`

## 3. Création d'une application
`python manage.py startapp polls`


* Définir les modèles dans le fichier `models.py`
* Ajouter l'application dans `INSTALLED_APPS` dans le fichier `settings.py`


## 4. Création des nouvelles tables
`python manage.py makemigrations polls`

`python manage.py migrate`

* Créer un fichier `polls/urls.py`
* 


## 5. Lancer le projet
`$ python manage.py runserver`




# DRF
```python
from polls.serializers import PollSerializer
from polls.models import Poll

# create
poll_serializer = PollSerializer(data={"question": "Mojito or Caipirinha?", "created_by": 1})
print(poll_serializer.is_valid())

poll = poll_serializer.save()
print(poll.pk)

# update
poll_serializer = PollSerializer(instance=poll, data={"question": "Mojito, Caipirinha or margarita?", "created_by": 1})
print(poll_serializer.is_valid())

poll_serializer.save()
print(Poll.objects.get(pk=5).question)
```


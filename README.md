# database_with_dango-simple-history
######
Avec mon collègue, Félix Mortas, nous avons créé une base de données dans le but de mettre en pratique django-simple-history (https://django-simple-history.readthedocs.io/) qui crée un historique de toute les modifications/création/supression dans une base de données. Nous nous sommes inspirer du travail de Thibault Latrille (https://github.com/ThibaultLatrille/MonPotager) qui a pu nous éclairer dans nos recherches et nous étions supervisés par Eric Tannier (Directeur de recherche)
######

installer Django (https://docs.djangoproject.com/fr/1.8/howto/windows/)                                                               

>> import Django

$ django-admin startproject bdd_potager

$ python manage.py startapp especes

$ python manage.py startapp interactions

On suit la documentation ('https://django-simple-history.readthedocs.io/en/latest/quick_start.html') pour installer simple-history dans le fichier "settings.py"

On créer notre table 'Espece' dans le dossier "especes", fichier "models.py"

On modifie le fichier "admin.py" pour gérer l'historique depuis l'interface Admin

On créer nos tests unitaires dans le fichier "tests.py" du dossier especes

$ python manage.py makemigrations 

$ python manage.py migrate

$ python manage.py test #commande pour faire les tests unitaires

$ python manage.py createsuperuser #Pour gérer l'interface Admin de Django, se souvenir de l'identifiant et du password

$ python manage.py runserver #Server lancé en local, ouvrir page internet "http://127.0.0.1:8000/"

http://127.0.0.1:8000/admin -> pour gérer l'interface administrateur


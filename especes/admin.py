from simple_history import register
from especes.models import Especes
from django.contrib.auth.models import User
from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

register(User)

class EspecesHistoryAdmin(SimpleHistoryAdmin):
    list_display = ['nom_commun', 'nom', 'category']
    history_list_display = ["statut"]
    
admin.site.register(Especes, EspecesHistoryAdmin)

from simple_history import register
from especes.models import Interactions
from django.contrib.auth.models import User
from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

register(User)

class InteractionsHistoryAdmin(SimpleHistoryAdmin):
	list_display = ["id", "source", "target", "interaction", "references"]
	history_list_display = ["statut"]

admin.site.register(Interactions, InteractionsHistoryAdmin)

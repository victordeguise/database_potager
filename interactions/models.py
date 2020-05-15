from django.db import models
from simple_history.models import HistoricalRecords


class Interaction(models.Model):
	__tablename__ = 'interactions'
	source = models.CharField(max_length = 255, null = False, verbose_name = "Celui qui donne l'interaction", blank = False)
	target = models.CharField(max_length = 255, null = False, verbose_name = "Celui qui reçoit l'interaction", blank = False)
	interaction = models.CharField(max_length = 255, null = False, verbose_name = "Type d'interaction", blank = False)
	references = models.URLField(max_length = 255, null = True, verbose_name = "Lien vers la source de l'interaction", blank = True)
	
class Meta:
	verbose_name = "Intéraction"
	ordering = ["interaction"]

    def __init__(self, source, target, interaction, references):
        self.source = source
        self.target = target
        self.interaction = interaction
        self.references = references
                                                                                           
    def serialize(self):
        return {
            'id': self.id,
            'source': self.source,
            'target': self.target,
            'interaction': self.interaction,
            'references': self.references
        }

from django.db import models
from simple_history.models import HistoricalRecords
    
class Especes(models.Model):
    nom = models.CharField(
        max_length=255,
        null=False,
        unique=True,
        verbose_name="Nom de l'espèce",
        blank=False #champ non vide
        )
    nom_commun = models.CharField(
        max_length=255,
        null=False,
        verbose_name="Nom commun de l'espèce",
        blank=False #champ non vide
        )
    category = models.CharField(
        max_length=255,
        null=False,
        verbose_name="categorie de l'espèce",
        blank=True #champ peut être vide
        )
    wiki = models.URLField(
        max_length=255,
        null=True,
        verbose_name="lien wikipedia",
        blank=True #champ peut être vide
        )
    taxonomy = models.IntegerField(
        null=True,
        blank=True,
        )
    NCBI = models.CharField(
        max_length=255,
        null=True,
        verbose_name="NCBI de l'espèce",
        blank=True 
        )
    history=HistoricalRecords()

    class Meta:
        r"""
        Options de métadonnées attribué au modèle.
        Les métadonnées de modèles sont « tout ce qui 
        n’est pas un champ », comme les options de tri (ordering),
        le nom de la table de base de données (db_table) ou 
        des noms verbeux singulier et pluriel 
        (verbose_name et verbose_name_plural). 
        Aucune n’est obligatoire et la présence de class Meta 
        dans un modèle est entièrement facultative.
        """
        verbose_name = 'Espèce'
        ordering = ['nom']
        
    def str(self):
        r"""
        Méthode permettant d'afficher plus joliment notre objet
        """
        return self.nom_commun or 'Aucun nom'
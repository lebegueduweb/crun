from hashlib import sha1
from pyexpat import model
from sqlite3 import TimestampFromTicks
from typing_extensions import Required
from django.db import models
from django.apps import apps
from django.urls import reverse
import uuid
from datetime import date
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django.forms import ModelForm


class Examen(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, help_text="Unique ID for this particular patient across whole library")
    Projet = models.CharField(max_length=50, default= "VAC078")
    Id_projet = models.CharField(max_length=50, blank=False, default="1", help_text="Entrez Id du participant dans le projet")
    Prénoms = models.CharField(max_length=200)
    Nom_de_famille = models.CharField(max_length=75)
    LAB_TEAM = (
        ('P', 'Parasitologie'),
        ('H', 'Hematology'),
        ('I', 'Immunologie'),
        ('B', 'Biochimie'),
        ('M', 'Microbiologie'),
      
    )
    EXAMEN_DICT = (
        ('Goute epaisse', 'Goute epaisse'),
        ('PCR', 'PCR'),
        ('NFS', 'NFS'),
        ('CRP', 'CRP'),
        ('Ionnogramme sanguin', 'Ionnogramme sanguin'),
        ('Triglycerides', 'Triglycerides'),
        ('Coproculture', 'Coproculture'),
        ('Hemoculture', 'Hemoculture'),
        ('Uroculture', 'Uroculture'),
        ('LCS', 'LCS'),
        ('Ecouvillonnage', 'Ecouvillonnage'),
        ('Liquide ascite', 'Liquide ascite'),
      
    )
    AGE_UNITS = (
        ('jours', 'jours'),
        ('Mois', 'Mois'),
        ('ans', 'ans'),
      
    )
    age = models.PositiveIntegerField(default="2", help_text='Entrer age du patien (en années)')
    temps = models.CharField(max_length=20, choices=AGE_UNITS, blank=True, default='m', help_text='Selectionner')
    SEXE_STATUS = (
        ('m', 'Masculin'),
        ('f', 'Feminin'),
      
    )
    def merge(self):
        age = age + temps
        print(age)
    sexe = models.CharField(max_length=10, choices=SEXE_STATUS, blank=True, default='m', help_text='Selectionner le genre')
    def get_absolute_url(self):
        """Returns the url to access a particular instance of Patient."""
        return reverse('examen_detail', args=[str(self.id)])

    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
        return  (self.Id_projet) 

    section = MultiSelectField(choices=LAB_TEAM, max_length=20)
    examen = MultiSelectField(choices=EXAMEN_DICT, max_length=100)
    prescipteur = models.CharField(default="Dr Ouedraogo", max_length=50)
    date_et_heure_de_demande = models.DateTimeField(auto_now=False, auto_now_add=False, )
    renseignements_cliniques = models.TextField(default="fièvre, vomissement")
    Autheur = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

class Archivage(models.Model):
    TYPE_ECHANTILLON = (
        ('sang', 'sang'),
        ('Serum', 'Serum'),
        ('Plasma', 'Plasma'),
        ('PCR', 'PCR'),
        ('Lame', 'Lame'),
        ('LCS', 'LCS'),
        ('Souche', 'Souche'),
        ('Autres', 'Autres'),
    )
    id_examen = models.UUIDField(primary_key=True, blank=True, default=uuid.uuid1, help_text="Unique ID for this particular patient across whole library")
    Type_echantillon = models.CharField(max_length=10, choices=TYPE_ECHANTILLON, blank=False, default='sang', help_text='Selectionner le type échantillon à archiver')
    Projet = models.CharField(max_length=50)
    id_projet = models.OneToOneField('Examen', default="NFS", on_delete=models.CASCADE, null=True)
    Réfrigérateur = models.CharField(max_length=50)
    Etude = models.CharField(max_length=100, default="A quel etude appartient echantillon?")
    Rangée = models.PositiveIntegerField()
    Boite = models.PositiveIntegerField()
    Position = models.PositiveIntegerField()
    Date_et_heure_archivage = models.DateTimeField(auto_now=False, auto_now_add=False,)
    Autheur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
        return '%s %s %s %s' % (self.id_examen,  self.id_projet, self.Réfrigérateur, self.Etude)
class ExamenForm(ModelForm):
    class Meta:
        model = Examen
        fields = ['id',"section", 'Id_projet', 'examen', 'age', 'prescipteur', "date_et_heure_de_demande", "renseignements_cliniques"]
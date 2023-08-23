from django.contrib import admin
from .models import Examen, Archivage

# Register your models here.
class ExamenAdmin(admin.ModelAdmin):
    model = Examen
    list_display = ['id', "section", 'Id_projet', 'examen', 'age', 'prescipteur', "date_et_heure_de_demande", "renseignements_cliniques"]
    fields = ['id',"section", 'Id_projet', 'examen', 'age', 'prescipteur', "date_et_heure_de_demande", "renseignements_cliniques"]

class ArchivageAdmin(admin.ModelAdmin):
    model = Archivage
    list_display = ['id_projet',  "Type_echantillon", 'Réfrigérateur', 'Rangée', 'Boite', 'Position', "Date_et_heure_archivage"]
    fields = [ 'id_projet',"Type_echantillon", 'Réfrigérateur', 'Rangée', 'Boite', 'Position', "Date_et_heure_archivage"]
admin.site.register(Examen, ExamenAdmin)
admin.site.register (Archivage, ArchivageAdmin)




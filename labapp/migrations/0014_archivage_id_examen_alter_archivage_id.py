# Generated by Django 4.2.4 on 2023-08-19 22:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('labapp', '0013_rename_auteur_archivage_autheur_archivage_etude'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivage',
            name='id_examen',
            field=models.UUIDField(blank=True, default=uuid.uuid1, help_text='Unique ID for this particular patient across whole library', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='archivage',
            name='id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='labapp.examen'),
        ),
    ]
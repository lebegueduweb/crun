# Generated by Django 4.2.4 on 2023-08-19 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('labapp', '0016_alter_archivage_id_projet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivage',
            name='id_projet',
            field=models.OneToOneField(default='NFS', null=True, on_delete=django.db.models.deletion.SET_NULL, to='labapp.examen'),
        ),
    ]
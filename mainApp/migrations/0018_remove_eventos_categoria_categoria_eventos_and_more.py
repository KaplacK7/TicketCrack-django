# Generated by Django 5.0.4 on 2025-05-29 19:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0017_remove_categoria_eventos_remove_categoria_funcion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventos',
            name='categoria',
        ),
        migrations.AddField(
            model_name='categoria',
            name='eventos',
            field=models.ManyToManyField(related_name='categorias', to='mainApp.eventos'),
        ),
        migrations.AddField(
            model_name='categoria',
            name='funcion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.funcion'),
        ),
    ]

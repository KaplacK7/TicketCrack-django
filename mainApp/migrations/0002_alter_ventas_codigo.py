# Generated by Django 5.0.4 on 2025-05-23 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventas',
            name='codigo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

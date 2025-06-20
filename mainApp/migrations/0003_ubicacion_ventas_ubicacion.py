# Generated by Django 5.0.4 on 2025-05-23 17:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_alter_ventas_codigo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.PositiveIntegerField()),
                ('asientos_disponibles', models.PositiveIntegerField()),
                ('asientos_vendidos', models.PositiveIntegerField(default=0)),
                ('funcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.funcion')),
            ],
        ),
        migrations.AddField(
            model_name='ventas',
            name='ubicacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.ubicacion'),
        ),
    ]

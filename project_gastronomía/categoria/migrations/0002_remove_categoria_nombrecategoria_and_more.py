# Generated by Django 4.2.5 on 2023-11-23 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='nombreCategoria',
        ),
        migrations.AddField(
            model_name='categoria',
            name='tipoCategoria',
            field=models.CharField(choices=[('sabor', 'Sabor'), ('dieta', 'Dieta')], default='región', max_length=20),
        ),
    ]

# Generated by Django 3.2 on 2023-12-02 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredientes', '0006_remove_ingredientes_cantidad'),
        ('carrito', '0002_auto_20231201_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito',
            name='Id_ingredientes',
        ),
        migrations.AddField(
            model_name='carrito',
            name='Id_ingredientes',
            field=models.ManyToManyField(to='ingredientes.Ingredientes'),
        ),
    ]

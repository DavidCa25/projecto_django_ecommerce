# Generated by Django 3.2 on 2023-12-05 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredientes', '0006_remove_ingredientes_cantidad'),
        ('compras', '0002_compra_nombre_compra_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='compra',
            field=models.ManyToManyField(to='ingredientes.Ingredientes'),
        ),
    ]

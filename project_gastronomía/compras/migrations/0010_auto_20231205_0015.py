# Generated by Django 3.2 on 2023-12-05 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0004_auto_20231202_2102'),
        ('compras', '0009_alter_compra_id_carrito'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='Id_carrito',
        ),
        migrations.AddField(
            model_name='compra',
            name='Id_carrito',
            field=models.ManyToManyField(to='carrito.Carrito'),
        ),
    ]

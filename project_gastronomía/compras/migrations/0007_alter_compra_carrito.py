# Generated by Django 3.2 on 2023-12-05 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0004_auto_20231202_2102'),
        ('compras', '0006_auto_20231205_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='carrito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrito.carrito'),
        ),
    ]

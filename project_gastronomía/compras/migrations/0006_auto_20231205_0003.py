# Generated by Django 3.2 on 2023-12-05 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0004_auto_20231202_2102'),
        ('compras', '0005_auto_20231204_2352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='carrito',
        ),
        migrations.AddField(
            model_name='compra',
            name='carrito',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='carrito.carrito'),
        ),
    ]

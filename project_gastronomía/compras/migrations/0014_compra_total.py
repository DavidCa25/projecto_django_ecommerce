# Generated by Django 3.2 on 2023-12-05 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0013_remove_compra_id_carrito'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]

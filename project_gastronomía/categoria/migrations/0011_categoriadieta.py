# Generated by Django 4.2.5 on 2023-11-24 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0010_delete_categoriadieta'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaDieta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('categoriaDieta', models.CharField(choices=[('mediterranea', 'Mediterranea'), ('vegetariana', 'Vegetariana'), ('Vegana', 'Vegana'), ('cetogénica', 'Cetogénica')], max_length=20)),
            ],
        ),
    ]

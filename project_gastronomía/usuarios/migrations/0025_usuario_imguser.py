# Generated by Django 3.2 on 2023-11-25 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0024_alter_usuario_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='imgUser',
            field=models.ImageField(null=True, upload_to='usuarios'),
        ),
    ]

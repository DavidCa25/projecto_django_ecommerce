# Generated by Django 4.2.5 on 2023-11-22 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0020_rename_email_usuario_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='username',
            new_name='email',
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-22 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LoginFaceDetection', '0003_alter_users_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={},
        ),
        migrations.RenameField(
            model_name='users',
            old_name='photo',
            new_name='foto',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='user_name',
            new_name='usuario',
        ),
    ]

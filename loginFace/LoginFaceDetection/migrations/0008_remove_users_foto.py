# Generated by Django 4.0.3 on 2022-04-23 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LoginFaceDetection', '0007_alter_users_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='foto',
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-22 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginFaceDetection', '0005_alter_users_password_alter_users_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='foto',
            field=models.CharField(max_length=10, verbose_name='Foto'),
        ),
    ]

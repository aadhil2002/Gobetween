# Generated by Django 4.0.5 on 2022-09-19 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gobetween_app', '0006_user_registarion_usertype_delete_user_s'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertype',
            name='user',
        ),
        migrations.DeleteModel(
            name='user_registarion',
        ),
        migrations.DeleteModel(
            name='UserType',
        ),
    ]

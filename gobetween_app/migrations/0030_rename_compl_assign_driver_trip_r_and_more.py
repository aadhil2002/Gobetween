# Generated by Django 4.0.5 on 2022-10-07 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gobetween_app', '0029_assign_driver'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assign_driver',
            old_name='compl',
            new_name='trip_r',
        ),
        migrations.RemoveField(
            model_name='assign_driver',
            name='dept',
        ),
    ]

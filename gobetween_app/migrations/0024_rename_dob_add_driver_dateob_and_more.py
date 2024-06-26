# Generated by Django 4.0.5 on 2022-09-30 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gobetween_app', '0023_driver_request_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='add_driver',
            old_name='dob',
            new_name='DateOB',
        ),
        migrations.RenameField(
            model_name='add_driver',
            old_name='age',
            new_name='carname',
        ),
        migrations.RenameField(
            model_name='add_driver',
            old_name='licence_no',
            new_name='cartype',
        ),
        migrations.RenameField(
            model_name='add_driver',
            old_name='name',
            new_name='gender',
        ),
        migrations.AddField(
            model_name='add_driver',
            name='plateno',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
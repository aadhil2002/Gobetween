# Generated by Django 4.0.5 on 2022-10-28 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gobetween_app', '0062_delete_schedule_trip'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip_request',
            name='purpose',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

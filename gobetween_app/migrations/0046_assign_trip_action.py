# Generated by Django 4.0.5 on 2022-10-14 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gobetween_app', '0045_remove_location_add_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='assign_trip',
            name='action',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

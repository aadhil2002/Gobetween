# Generated by Django 4.2 on 2023-04-19 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gobetween_app', '0080_trip_request_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_vehicle',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gobetween_app.driver_reg'),
        ),
    ]
# Generated by Django 4.0.5 on 2022-10-15 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gobetween_app', '0048_add_vehicle_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_vehicle',
            name='veh_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gobetween_app.add_vehicle_type'),
        ),
    ]
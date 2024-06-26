# Generated by Django 4.0.5 on 2022-10-11 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gobetween_app', '0041_trip_request_company_alter_trip_request_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_vehicle',
            name='user',
        ),
        migrations.RemoveField(
            model_name='driver_reg',
            name='user',
        ),
        migrations.AddField(
            model_name='add_vehicle',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gobetween_app.comp_reg'),
        ),
        migrations.AddField(
            model_name='driver_reg',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gobetween_app.comp_reg'),
        ),
    ]
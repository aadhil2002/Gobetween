# Generated by Django 4.1.5 on 2023-03-25 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gobetween_app', '0071_remove_driver_request_user_driver_request_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver_request',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

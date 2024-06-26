# Generated by Django 4.0.5 on 2022-09-29 07:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gobetween_app', '0018_add_driver'),
    ]

    operations = [
        migrations.CreateModel(
            name='trip_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('pickup_place', models.CharField(max_length=100, null=True)),
                ('to_place', models.CharField(max_length=100, null=True)),
                ('mobile', models.CharField(max_length=100, null=True)),
                ('time', models.CharField(max_length=100, null=True)),
                ('date', models.DateField(max_length=100, null=True)),
                ('no_of_persons', models.CharField(max_length=100, null=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gobetween_app.comp_reg')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
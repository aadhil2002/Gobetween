# Generated by Django 4.2 on 2023-04-25 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gobetween_app', '0083_remove_driver_request_age_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='driver_leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdate', models.DateField(max_length=100, null=True)),
                ('enddate', models.DateField(max_length=100, null=True)),
                ('no_of_days', models.IntegerField(max_length=100, null=True)),
                ('reason', models.CharField(max_length=100, null=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gobetween_app.comp_reg')),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gobetween_app.driver_reg')),
            ],
        ),
    ]

# Generated by Django 4.0.5 on 2022-09-20 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gobetween_app', '0013_comp_reg'),
    ]

    operations = [
        migrations.AddField(
            model_name='comp_reg',
            name='company_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

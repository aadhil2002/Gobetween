# Generated by Django 4.0.5 on 2022-09-20 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gobetween_app', '0014_comp_reg_company_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_reg',
            old_name='DOB',
            new_name='DateOfBirth',
        ),
        migrations.RemoveField(
            model_name='comp_reg',
            name='DOB',
        ),
        migrations.RemoveField(
            model_name='comp_reg',
            name='gender',
        ),
    ]

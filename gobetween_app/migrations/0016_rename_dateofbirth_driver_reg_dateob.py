# Generated by Django 4.0.5 on 2022-09-22 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gobetween_app', '0015_rename_dob_user_reg_dateofbirth_remove_comp_reg_dob_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driver_reg',
            old_name='DateOfBirth',
            new_name='DateOB',
        ),
    ]
# Generated by Django 4.2 on 2023-04-30 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gobetween_app', '0087_remove_complaint_email_remove_complaint_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
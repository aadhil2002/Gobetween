# Generated by Django 4.0.5 on 2022-10-11 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gobetween_app', '0040_d_feedback_c_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip_request',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gobetween_app.comp_reg'),
        ),
        migrations.AlterField(
            model_name='trip_request',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='assign_trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100, null=True)),
                ('comp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gobetween_app.comp_reg')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gobetween_app.driver_reg')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gobetween_app.trip_request')),
                ('veh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gobetween_app.add_vehicle')),
            ],
        ),
    ]
# Generated by Django 3.2.7 on 2021-09-23 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0007_alter_touristspot_counting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toruistimg',
            name='Touristspot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='img', to='tour.touristspot'),
        ),
    ]

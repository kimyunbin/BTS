# Generated by Django 3.2.7 on 2021-09-27 06:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0008_alter_toruistimg_touristspot'),
        ('accounts', '0006_alter_user_nickname'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Touristspot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.touristspot')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

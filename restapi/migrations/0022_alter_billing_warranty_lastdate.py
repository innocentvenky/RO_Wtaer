# Generated by Django 4.1.13 on 2024-10-16 05:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0021_alter_servicing_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='warranty_lastdate',
            field=models.DateField(default=datetime.date(2025, 10, 16)),
        ),
    ]
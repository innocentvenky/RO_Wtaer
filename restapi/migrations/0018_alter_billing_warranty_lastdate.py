# Generated by Django 4.1.13 on 2024-07-01 13:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0017_alter_billing_data_alter_billing_warranty_lastdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='warranty_lastdate',
            field=models.DateField(default=datetime.date(2025, 7, 1)),
        ),
    ]

# Generated by Django 4.1.13 on 2024-06-28 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0009_rename_phonne_number_address_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='full_name',
            field=models.CharField(max_length=500),
        ),
    ]

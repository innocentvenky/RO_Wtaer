# Generated by Django 4.1.13 on 2024-07-01 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0020_servicing_user_id_alter_address_user_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicing',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

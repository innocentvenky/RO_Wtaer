# Generated by Django 4.1.13 on 2024-06-28 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0004_rename_user_image_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('public_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('feedback', models.TextField()),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PurifierModel',
            fields=[
                ('public_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('model_name', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='PurifierDetails',
            fields=[
                ('public_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='images/')),
                ('capacity', models.TextField()),
                ('color', models.CharField(max_length=500)),
                ('purification_features', models.TextField()),
                ('installation_type', models.CharField(max_length=500)),
                ('filtration_capacity', models.CharField(max_length=500)),
                ('power_requirement', models.CharField(max_length=500)),
                ('purification_technology', models.CharField(max_length=600)),
                ('width', models.CharField(max_length=300)),
                ('height', models.CharField(max_length=300)),
                ('depth', models.CharField(max_length=300)),
                ('weight', models.CharField(max_length=300)),
                ('warranty_summary', models.CharField(max_length=500)),
                ('warranty_service_type', models.CharField(max_length=500)),
                ('domestic_warranty', models.CharField(max_length=600)),
                ('purifiermodel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purifier_details', to='restapi.purifiermodel')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('public_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('building_name', models.TextField()),
                ('area', models.TextField()),
                ('nearby', models.TextField()),
                ('city', models.TextField()),
                ('state', models.TextField()),
                ('pincode', models.CharField(max_length=6)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Address', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

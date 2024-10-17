# Generated by Django 4.1.13 on 2024-07-01 10:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0012_alter_address_full_name_alter_address_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('public_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('full_name', models.CharField(default='none', max_length=250)),
                ('phone_number', models.CharField(default='none', max_length=15)),
                ('Problem', models.TextField()),
                ('images', models.ImageField(upload_to='photos/Issues_images/')),
            ],
        ),
        migrations.AddField(
            model_name='purifierdetails',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='purifierdetails',
            name='image',
            field=models.ImageField(upload_to='photos/purifier_images/'),
        ),
        migrations.AlterField(
            model_name='purifiermodel',
            name='image',
            field=models.ImageField(upload_to='photos/profile_images/'),
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('public_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cost', models.FloatField(default=0.0)),
                ('CGST', models.FloatField()),
                ('SGST', models.FloatField()),
                ('total', models.FloatField(default=0.0)),
                ('purifierdetails_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cost', to='restapi.purifierdetails')),
            ],
        ),
    ]

# Generated by Django 4.1.13 on 2024-06-28 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0003_rename_images_image_image_rename_user_id_image_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='user',
            new_name='user_id',
        ),
    ]

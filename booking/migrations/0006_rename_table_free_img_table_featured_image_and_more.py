# Generated by Django 4.0.5 on 2022-07-08 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_rename_featured_image_table_table_free_img_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table',
            old_name='table_free_img',
            new_name='featured_image',
        ),
        migrations.RemoveField(
            model_name='table',
            name='table_occupied_img',
        ),
    ]

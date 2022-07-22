# Generated by Django 4.0.6 on 2022-07-22 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_alter_review_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='time_created_on',
        ),
        migrations.RemoveField(
            model_name='review',
            name='time_updated_on',
        ),
        migrations.AlterField(
            model_name='review',
            name='date_created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='date_updated_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
# Generated by Django 4.1 on 2022-08-18 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_alter_review_date_created_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date_created_on',
            field=models.DateTimeField(default='2022-08-18 13:07:35'),
        ),
        migrations.AlterField(
            model_name='review',
            name='date_updated_on',
            field=models.DateTimeField(default='2022-08-18 13:07:35'),
        ),
    ]

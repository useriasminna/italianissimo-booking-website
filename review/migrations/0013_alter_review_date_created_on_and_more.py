# Generated by Django 4.1 on 2022-08-25 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0012_alter_review_date_created_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date_created_on',
            field=models.DateTimeField(default='2022-08-25 14:18:53'),
        ),
        migrations.AlterField(
            model_name='review',
            name='date_updated_on',
            field=models.DateTimeField(default='2022-08-25 14:18:53'),
        ),
    ]

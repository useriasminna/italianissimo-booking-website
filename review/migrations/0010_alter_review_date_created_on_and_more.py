# Generated by Django 4.1 on 2022-08-20 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0009_alter_review_date_created_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date_created_on',
            field=models.DateTimeField(default='2022-08-20 17:17:28'),
        ),
        migrations.AlterField(
            model_name='review',
            name='date_updated_on',
            field=models.DateTimeField(default='2022-08-20 17:17:28'),
        ),
    ]
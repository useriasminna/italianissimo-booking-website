# Generated by Django 4.1 on 2022-08-18 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0014_alter_booking_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='created_on',
            field=models.DateTimeField(blank=True),
        ),
    ]
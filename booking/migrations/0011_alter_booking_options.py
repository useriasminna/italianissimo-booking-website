# Generated by Django 4.0.6 on 2022-07-20 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_booking_created_by'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['date', 'start_time']},
        ),
    ]

# Generated by Django 4.0.5 on 2022-07-01 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_table_no_of_persons'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='persons_number',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='slug',
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-26 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='ingredients',
            field=models.CharField(default='ingredients', max_length=1000),
            preserve_default=False,
        ),
    ]
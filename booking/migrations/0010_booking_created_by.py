# Generated by Django 4.0.6 on 2022-07-19 11:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0009_alter_booking_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='created_by',
            field=models.ForeignKey(blank=True, default=4, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='email'),
            preserve_default=False,
        ),
    ]

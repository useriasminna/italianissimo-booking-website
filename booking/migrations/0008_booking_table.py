# Generated by Django 4.0.5 on 2022-07-08 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_remove_table_featured_image_table_table_free_img_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='table',
            field=models.ForeignKey(default='Table', on_delete=django.db.models.deletion.CASCADE, to='booking.table', to_field='code'),
            preserve_default=False,
        ),
    ]

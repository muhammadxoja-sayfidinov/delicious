# Generated by Django 3.1.7 on 2021-03-15 15:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dlc_app', '0015_auto_20210315_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='recept',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

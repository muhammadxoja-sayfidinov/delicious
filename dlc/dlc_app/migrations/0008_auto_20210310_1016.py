# Generated by Django 3.1.7 on 2021-03-10 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dlc_app', '0007_recept'),
    ]

    operations = [
        migrations.AddField(
            model_name='recept',
            name='ings',
            field=models.JSONField(default={}),
        ),
        migrations.AddField(
            model_name='recept',
            name='steps',
            field=models.JSONField(default={'steps': []}),
        ),
    ]
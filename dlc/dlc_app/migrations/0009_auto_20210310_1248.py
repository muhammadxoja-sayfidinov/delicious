# Generated by Django 3.1.7 on 2021-03-10 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dlc_app', '0008_auto_20210310_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='recept',
            name='image2',
            field=models.ImageField(null=True, upload_to='news_image'),
        ),
        migrations.AddField(
            model_name='recept',
            name='image3',
            field=models.ImageField(null=True, upload_to='news_image'),
        ),
    ]
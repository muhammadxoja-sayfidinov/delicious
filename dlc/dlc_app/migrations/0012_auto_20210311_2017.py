# Generated by Django 3.1.7 on 2021-03-11 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dlc_app', '0011_auto_20210311_1839'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.SmallIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='recept',
            name='category',
            field=models.SmallIntegerField(default=1),
        ),
    ]

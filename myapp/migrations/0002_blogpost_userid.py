# Generated by Django 3.2.14 on 2022-07-26 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='userid',
            field=models.IntegerField(default=0),
        ),
    ]

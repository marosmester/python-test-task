# Generated by Django 3.2.14 on 2022-07-29 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_blogpost_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

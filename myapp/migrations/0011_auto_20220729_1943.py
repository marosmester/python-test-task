# Generated by Django 3.2.14 on 2022-07-29 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20220729_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='userId',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 2.0.4 on 2018-05-01 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0009_auto_20180501_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]

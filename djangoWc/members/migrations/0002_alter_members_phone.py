# Generated by Django 4.1.6 on 2023-03-13 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='phone',
            field=models.IntegerField(),
        ),
    ]

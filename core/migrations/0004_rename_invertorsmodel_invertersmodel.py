# Generated by Django 5.1.7 on 2025-04-28 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_batterymodel_alter_invertorsmodel_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InvertorsModel',
            new_name='InvertersModel',
        ),
    ]

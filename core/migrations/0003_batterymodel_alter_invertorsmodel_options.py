# Generated by Django 5.1.7 on 2025-04-25 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_invertorsmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='BatteryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Ady')),
                ('price', models.FloatField(default=0.0, verbose_name='Bahasy')),
            ],
            options={
                'verbose_name': 'Batareýa',
                'verbose_name_plural': 'Batareýalar',
            },
        ),
        migrations.AlterModelOptions(
            name='invertorsmodel',
            options={'verbose_name': 'Inwentor', 'verbose_name_plural': 'Inwentorlar'},
        ),
    ]

# Generated by Django 5.2 on 2025-06-05 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_wastereport_latitude_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wastereport',
            name='image',
        ),
    ]

# Generated by Django 4.1.2 on 2022-11-03 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='meeting',
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-31 22:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0008_alter_meeting_max_ppl_alter_meeting_min_ppl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='players',
            field=models.ManyToManyField(related_name='user_playing', to=settings.AUTH_USER_MODEL),
        ),
    ]
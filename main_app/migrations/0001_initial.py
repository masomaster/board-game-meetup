# Generated by Django 4.1.2 on 2022-10-28 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('min_player', models.IntegerField()),
                ('max_player', models.IntegerField()),
                ('avg_game_play', models.IntegerField()),
                ('difficulty_rating', models.IntegerField()),
                ('genre', models.CharField(max_length=50)),
                ('min_age', models.IntegerField(default=5)),
            ],
        ),
    ]

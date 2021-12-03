# Generated by Django 3.2.9 on 2021-12-03 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField()),
                ('movie_name', models.CharField(max_length=40)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]

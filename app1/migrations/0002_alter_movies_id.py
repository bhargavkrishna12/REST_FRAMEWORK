# Generated by Django 3.2.9 on 2021-11-26 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

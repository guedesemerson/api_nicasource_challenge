# Generated by Django 4.2.1 on 2023-05-26 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0002_initial'),
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.ManyToManyField(to='rating.rating'),
        ),
    ]
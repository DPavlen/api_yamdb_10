# Generated by Django 3.2 on 2023-06-13 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='titles',
            name='genres',
            field=models.ManyToManyField(to='reviews.Genre'),
        ),
    ]

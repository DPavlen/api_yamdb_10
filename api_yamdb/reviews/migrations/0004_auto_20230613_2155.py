# Generated by Django 3.2 on 2023-06-13 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_alter_titles_year'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='titles',
            options={'verbose_name': ('Произведение',), 'verbose_name_plural': ('Произведения',)},
        ),
        migrations.RemoveField(
            model_name='titles',
            name='genres',
        ),
    ]

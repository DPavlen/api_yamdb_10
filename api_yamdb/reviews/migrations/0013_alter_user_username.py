# Generated by Django 3.2 on 2023-06-15 14:06

from django.db import migrations, models
import reviews.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0012_titles_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, unique=True, validators=[reviews.validators.UsernameValidatorRegex(), reviews.validators.username_me], verbose_name='Имя пользователя'),
        ),
    ]
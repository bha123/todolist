# Generated by Django 3.2.5 on 2022-01-28 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0006_auto_20220128_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='deleteitem',
            name='autoCompletePomodoro',
            field=models.BooleanField(default=0, verbose_name='Pomodoro Complete'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='autoCompletePomodoro',
            field=models.BooleanField(default=0, verbose_name='Pomodoro Complete'),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.1.7 on 2021-03-15 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='pomodoro_estimate',
            field=models.IntegerField(default=3, verbose_name='Pomodoro Estimate'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='create_date',
            field=models.DateTimeField(verbose_name='Date created'),
        ),
    ]

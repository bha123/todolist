# Generated by Django 3.1.7 on 2021-03-16 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_item_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='pomodoro_completed',
            field=models.IntegerField(default=0, verbose_name='Pomodoro Completed'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.5 on 2022-01-28 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_auto_20220128_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deleteitem',
            name='autoCompletePomodoro',
        ),
        migrations.RemoveField(
            model_name='item',
            name='autoCompletePomodoro',
        ),
    ]

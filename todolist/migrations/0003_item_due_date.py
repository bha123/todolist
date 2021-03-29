# Generated by Django 3.1.7 on 2021-03-16 06:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_auto_20210315_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='due_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Due date'),
            preserve_default=False,
        ),
    ]

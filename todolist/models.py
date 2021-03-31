from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Item(models.Model):
    # create  a list item todo
    todo_item = models.CharField(max_length=700)
    create_date = models.DateTimeField('Date created')
    due_date = models.DateTimeField('Due date')
    status = models.BooleanField('Completed')
    pomodoro_estimate = models.IntegerField('Pomodoro Estimate')
    pomodoro_completed = models.IntegerField('Pomodoro Completed')
    recurring_task = models.BooleanField('Recurring')

    def __str__(self):
        return self.todo_item

    
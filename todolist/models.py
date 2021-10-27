from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

class CustomUser(models.Model):
    username = models.CharField(max_length=70)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    profile_name = models.CharField(max_length=70)
    def __str__(self):
        return self.username


# Create your models here
# .
class Item(models.Model):
    # create  a list item todo
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    user  = models.ForeignKey(User, on_delete= models.CASCADE)
    todo_item = models.CharField(max_length=700)
    create_date = models.DateTimeField('Date created')
    start_date = models.DateTimeField('Date started',null=True)
    due_date = models.DateTimeField('Due date')
    status = models.BooleanField('Completed')
    pomodoro_estimate = models.IntegerField('Pomodoro Estimate')
    pomodoro_completed = models.IntegerField('Pomodoro Completed')
    recurring_task = models.BooleanField('Recurring')
    itemPriority = models.IntegerField('priority')
    tags = models.CharField(max_length=100)

    def __str__(self):
        return self.todo_item

# Create your models here.
class DeleteItem(models.Model):
    # create  a list item todo
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    user  = models.ForeignKey(User, on_delete= models.CASCADE)
    todo_item = models.CharField(max_length=700)
    create_date = models.DateTimeField('Date created')
    start_date = models.DateTimeField('Date started',null=True)
    due_date = models.DateTimeField('Due date')
    status = models.BooleanField('Completed')
    pomodoro_estimate = models.IntegerField('Pomodoro Estimate')
    pomodoro_completed = models.IntegerField('Pomodoro Completed')
    recurring_task = models.BooleanField('Recurring')    
    itemPriority = models.IntegerField('priority')
    tags = models.CharField(max_length=100)

    def __str__(self):
        return self.todo_item



class dateStatusCheck(models.Model):
    today_date = models.DateField('Today Date')
    def __str__(self):
        return self.today_date.strftime('%Y-%m-%d')


class RecurringItemStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    #item_id = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='todo_item_recur')
    item_id = models.IntegerField('Item')
    pomodoro_completed = models.IntegerField('Pomodoro Completed')
    pomodoro_estimated = models.IntegerField('Pomodoro Estimate')
    event_time  = models.DateTimeField('Event Timestamp')
    def __str__(self):
        return self.todo_item


class telegrambotUserMapping(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    telebotId = models.TextField('telegramId')
    event_time = models.DateTimeField('Event Timestamp')

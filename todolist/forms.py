from django import forms
import datetime
from .models import Item
from .models import CustomUser
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.admin import widgets

class ItemForm(forms.Form):
    todo_item =  forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20})) 
    start_date = forms.DateTimeField(initial=datetime.date.today)  
    recurring_task = forms.BooleanField(required=False,widget=forms.RadioSelect())
    autoCompletePomodoro = forms.BooleanField(required=False,widget=forms.RadioSelect())
    due_date = forms.DateTimeField(initial=datetime.date.today)
    pomodoro_estimate = forms.IntegerField()
    pomodoro_completed = forms.IntegerField()
    itemPriority = forms.IntegerField()
    class Meta:
        model = Item
        fields = "__all__"


class ItemUpdateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
   

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = "__all__"



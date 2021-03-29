from django import forms
import datetime
from .models import Item

class ItemForm(forms.Form):
    #your_name = forms.CharField(label='Your name', max_length=100)
    #todo_item = forms.CharField(label=" Your Task", max_length=700)
    todo_item =  forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    create_date = forms.DateTimeField(initial=datetime.date.today)
    due_date = forms.DateTimeField(initial=datetime.date.today)
    #status = forms.BooleanField()
    pomodoro_estimate = forms.IntegerField()
    pomodoro_completed = forms.IntegerField()

class ItemUpdateForm(forms.Form):
    class Meta:
        model = Item
        fields = "__all__"


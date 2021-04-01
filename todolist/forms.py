from django import forms
import datetime
from .models import Item

class ItemForm(forms.Form):
    todo_item =  forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    #create_date = forms.DateTimeField(initial=datetime.date.today)
    
    #create_date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    
    recurring_task = forms.BooleanField(required=False)

    create_date = forms.DateTimeField(initial=datetime.date.today)
    
    due_date = forms.DateTimeField(initial=datetime.date.today)
    #status = forms.BooleanField()
    pomodoro_estimate = forms.IntegerField()
    pomodoro_completed = forms.IntegerField()
    class Meta:
        model = Item
        fields = "__all__"


class ItemUpdateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
   


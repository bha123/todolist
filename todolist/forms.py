from django import forms
import datetime
from .models import Item
from .models import CustomUser
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.admin import widgets

class ItemForm(forms.Form):
    todo_item =  forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    #todo_item = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    create_date = forms.DateTimeField(initial=datetime.date.today)
    
    #create_date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    
    recurring_task = forms.BooleanField(required=False,widget=forms.RadioSelect())

    #create_date = forms.DateTimeField(initial=datetime.date.today,widget=forms.SplitDateTimeWidget())
    
    '''
    create_date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
    '''

    due_date = forms.DateTimeField(initial=datetime.date.today)
    #status = forms.BooleanField()
    pomodoro_estimate = forms.IntegerField()
    pomodoro_completed = forms.IntegerField()
    class Meta:
        model = Item
        fields = "__all__"



'''
class ItemForm(forms.ModelForm):
    class Meta(object):
        model = Item
        #fields = ('todo_item','recurring_task','create_date','due_date','pomodoro_estimate','pomodoro_completed')
        fields = ['todo_item','recurring_task','create_date','due_date','pomodoro_estimate','pomodoro_completed']
        widgets = {
            'todo_item': forms.Textarea(attrs={'class': 'form-control'}),
            'create_date':  widgets.AdminSplitDateTime,
            
        }
'''
'''
class ItemForm():
    todo_item = forms.CharField(label='todo_item', max_length=100)

'''


class ItemUpdateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
   

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = "__all__"
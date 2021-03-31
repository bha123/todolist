from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item
from django import forms
from .forms import ItemForm, ItemUpdateForm
from django.shortcuts import redirect
from django.http import QueryDict
#from django.db.models import Item
# Create your views here.

def index(request):
    recurring_items = Item.objects.filter(recurring_task='1').order_by('status')
    
    list_of_items = Item.objects.filter(recurring_task='0').order_by('status')
    context = {'recurring_items': recurring_items, 'list_of_items': list_of_items,}
    return render(request, 'todolist/index.html', context)

def detail(request, item_id):
    task_item = get_object_or_404(Item, pk=item_id)
    return render(request, 'todolist/details.html', {'task_item': task_item})

def thanks(request):
    context = {}
    return  render(request, 'todolist/thanks.html', context)

def additem(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ItemForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # 
            # redirect to a new URL:
            #return HttpResponseRedirect('todolist/thanks/')
            #print(form.cleaned_data['todo_item'])
            
            todo_item = form.cleaned_data['todo_item']
            create_date = form.cleaned_data['create_date']           
            due_date = form.cleaned_data['due_date']            
            status = False
            pomodoro_estimate = form.cleaned_data['pomodoro_estimate']
            pomodoro_completed = form.cleaned_data['pomodoro_completed']
            recurring_task = form.cleaned_data['recurring_task']
            
            item = Item(todo_item=todo_item, create_date=create_date, due_date=due_date, status=status,
                         pomodoro_estimate=pomodoro_estimate,pomodoro_completed=pomodoro_completed)
            item.save()
            return redirect('/todolist/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ItemForm()

    return render(request, 'todolist/additem.html', {'form': form})

'''
def update_item_status(request):
    if request.method == 'POST':
        item_id = QueryDict(request.body)['id']
        
        present_status = QueryDict(request.body)['status']
        print("present status: ",present_status)
        
        if present_status == 'False':
            updated_status = True
        else:
            updated_status = False
        updateItem = ItemForm(Item.objects.get(id=item_id))
        
        print("updated status", updated_status)
        print(updateItem.todo_item)
        updateItem.status = updated_status
        updateItem.id = item_id
        #updateItem
        print(updateItem.status)
        updateItem.save()

        testItem = Item.objects.get(id=item_id)
        print(testItem)
     
    return HttpResponse("You updated the db status ")
'''

def update_item_status(request):
    if request.method == 'POST':
        item_id = int(QueryDict(request.body)['id'])
        updateItem = Item.objects.get(id=item_id)
        update_status = False
        present_status = updateItem.status
        if present_status == False:
            updated_status = True
        else:
            updated_status = False
        Item.objects.filter(pk=item_id).update(status=updated_status)
        
    return HttpResponse("You updated the db status ")




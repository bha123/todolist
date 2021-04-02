from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item, DeleteItem
from django import forms
from .forms import ItemForm, ItemUpdateForm
from django.shortcuts import redirect
from django.http import QueryDict, JsonResponse
from django.forms.models import model_to_dict
import json
#from django.db.models import Item
# Create your views here.

def index(request):
    recurring_items = Item.objects.filter(recurring_task='1').order_by('status') 
    completed_items = Item.objects.filter(status='1').order_by('pomodoro_estimate')   
    list_of_items = Item.objects.filter(recurring_task='0',status='0').order_by('-create_date')
    context = {'recurring_items': recurring_items, 'list_of_items': list_of_items, 'completed_items': completed_items,}
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
            if recurring_task == None:
                recurring_task = False
            
            item = Item(todo_item=todo_item, 
                        create_date=create_date, 
                        due_date=due_date, 
                        status=status,
                        recurring_task=recurring_task,
                        pomodoro_estimate=pomodoro_estimate,
                        pomodoro_completed=pomodoro_completed)
            item.save()
            return redirect('/todolist/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ItemForm()

    return render(request, 'todolist/additem.html', {'form': form})


def edit_item(request,id):
    if request.method == "POST":
        tobe_updated_item = Item.objects.get(id=id)
        item_keys = ['todo_item','create_date','due_date','status','recurring_task','pomodoro_estimate','pomodoro_completed']
        print(request.POST.get('status',False))
        Item.objects.filter(pk=id).update(
            todo_item=request.POST.get('todo_item'), 
            create_date=request.POST.get('create_date'), 
            due_date=request.POST.get('due_date'), 
            status= request.POST.get('status',False),
            recurring_task=request.POST.get('recurring_task', False),
            pomodoro_estimate=request.POST.get('pomodoro_estimate'),
            pomodoro_completed=request.POST.get('pomodoro_completed')
            )
        return redirect('/todolist/')
        
        
        
    if id:
        edit_item = Item.objects.get(id=id)
        form = ItemUpdateForm(instance=edit_item)

        print("showing the form")

        return render(request,'todolist/editItem.html',{'form':form})
    


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
        
    return redirect("You updated the db status ")




def deleteItem(request,id):

    item_id = id
    if item_id :
            # saving the deleted item in deleted table 
        deleted_item = Item.objects.get(id=item_id)
        deleteObj = DeleteItem(todo_item=deleted_item.todo_item, 
                               create_date=deleted_item.create_date, 
                               due_date=deleted_item.due_date, 
                               status=deleted_item.status, 
                               recurring_task=deleted_item.recurring_task,
                               pomodoro_estimate=deleted_item.pomodoro_estimate,
                               pomodoro_completed=deleted_item.pomodoro_completed)
        #deleteObj = DeletedItem(deleted_item)
        deleteObj.save()
        # delete it from items table 
        Item.objects.filter(pk=item_id).delete()
        return redirect('/todolist/')


def pomodoroTimer(request,id):
    print(id)
    item_id = id
    if item_id :
            # saving the deleted item in deleted table 
        pomodoro_item = Item.objects.get(id=item_id)

    return render(request,"todolist/pomodorotimer.html",{'item':pomodoro_item})


def updatePomodoroCount(request):
    if request.method == 'POST':
        print("reached pomodoro count")
        item_id = QueryDict(request.body)['id']
        print("update item id",item_id)
        
        pomodoro_item = Item.objects.get(id=item_id)
        print(pomodoro_item.pomodoro_completed)
        
        if pomodoro_item:
            count = pomodoro_item.pomodoro_completed  + 1
            print(count)
            Item.objects.filter(pk=item_id).update(pomodoro_completed=count)
            itemDict = {'id':item_id, 'pomdoro_completed':count}
            return HttpResponse(json.dumps(itemDict), content_type='application/json')           
            

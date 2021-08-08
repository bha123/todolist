from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item, DeleteItem, CustomUser,RecurringItemStatus, dateStatusCheck
from django import forms
from .forms import ItemForm, ItemUpdateForm, CustomUserForm
from django.shortcuts import redirect
from django.http import QueryDict, JsonResponse
from django.forms.models import model_to_dict
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import authenticate , login as loginUser , logout
import json
from django.contrib.auth.decorators import login_required
import datetime
#from django.db.models import Item
# Create your views here.

@login_required(login_url='login/')
def index(request):
    if request.user.is_authenticated:
        user = request.user
        print(user.username)
        recurring_items = Item.objects.filter(recurring_task='1',user=user).order_by('status') 
        completed_items = Item.objects.filter(status='1',user=user).order_by('pomodoro_estimate')   
        list_of_items = Item.objects.filter(recurring_task='0',user=user,status='0').order_by('-create_date')
        context = {'recurring_items': recurring_items, 'list_of_items': list_of_items, 'completed_items': completed_items, 'logged_user':user.username,}
        checkAndUpdateRecurringTask()
        return render(request, 'todolist/index.html', context)
    else:
        return redirect("/todolist/")


def detail(request, item_id):
    task_item = get_object_or_404(Item, pk=item_id)
    return render(request, 'todolist/details.html', {'task_item': task_item})

def thanks(request):
    context = {}
    return  render(request, 'todolist/thanks.html', context)


@login_required(login_url='login/')
def additem(request):

    if request.user.is_authenticated:
        user = request.user
        print(user)


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
                user = user
                todo_item = form.cleaned_data['todo_item']
                create_date = form.cleaned_data['create_date']           
                due_date = form.cleaned_data['due_date']            
                status = False
                pomodoro_estimate = form.cleaned_data['pomodoro_estimate']
                pomodoro_completed = form.cleaned_data['pomodoro_completed']
                recurring_task = form.cleaned_data['recurring_task']
                if recurring_task == None:
                    recurring_task = False
                itemPriority = form.cleaned_data['itemPriority']
                item = Item(todo_item=todo_item, 
                            create_date=create_date, 
                            due_date=due_date, 
                            status=status,
                            recurring_task=recurring_task,
                            pomodoro_estimate=pomodoro_estimate,
                            pomodoro_completed=pomodoro_completed,
                            user=user,
                            itemPriority=itemPriority)
                item.save()
                return redirect('todolist:index')

        # if a GET (or any other method) we'll create a blank form
        else:
            form = ItemForm()

        return render(request, 'todolist/additem.html', {'form': form})

@login_required(login_url='login/')
def edit_item(request,id):
    if request.user.is_authenticated:
        user = request.user
        if request.method == "POST":
            recurringStatus = status = False # 040 6810 2816 2845 2840
            if request.POST.get('recurring_task') == 'on':
                recurringStatus = True
            if request.POST.get('status') == 'on':
                status = True
            Item.objects.filter(pk=id).update(
                user = request.POST.get('user'),
                todo_item=request.POST.get('todo_item'), 
                create_date=request.POST.get('create_date'), 
                due_date=request.POST.get('due_date'), 
                status=status,
                recurring_task=recurringStatus,
                pomodoro_estimate=request.POST.get('pomodoro_estimate'),
                pomodoro_completed=request.POST.get('pomodoro_completed'),
                itemPriority=request.POST.get('itemPriority')
                )
            return redirect('todolist:index')
            
            
        if id:
            edit_item = Item.objects.get(id=id)
            form = ItemUpdateForm(instance=edit_item)
            print("showing the form")
            return render(request,'todolist/editItem.html',{'form':form})
        
@login_required(login_url='login/')
def update_item_status(request):
    if request.user.is_authenticated:
        user = request.user
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

@login_required(login_url='login/')
def reload_with_filter(request,id):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'GET':
            #filter_value = (QueryDict(request.body)['filter_value'])
            filter_value = id
            print(filter_value)
            print("entered reload with filter")
            if filter_value:
                recurring_items = Item.objects.filter(recurring_task='1',user=user,itemPriority=filter_value).order_by('status') 
                completed_items = Item.objects.filter(status='1',user=user,itemPriority=filter_value).order_by('pomodoro_estimate')   
                list_of_items = Item.objects.filter(recurring_task='0',user=user,status='0', itemPriority=filter_value).order_by('-create_date')
                context = {'recurring_items': recurring_items, 'list_of_items': list_of_items, 'completed_items': completed_items, 'logged_user':user.username,}
                checkAndUpdateRecurringTask()
                return render(request, 'todolist/index.html', context)
                
            else:
                return redirect("/todolist/")



@login_required(login_url='login/')
def deleteItem(request,id):

    item_id = id
    if item_id :
            # saving the deleted item in deleted table 
        user = request.user
        deleted_item = Item.objects.get(id=item_id)
        deleteObj = DeleteItem(
                               user=request.user,
                               todo_item=deleted_item.todo_item, 
                               create_date=deleted_item.create_date, 
                               due_date=deleted_item.due_date, 
                               status=deleted_item.status, 
                               recurring_task=deleted_item.recurring_task,
                               pomodoro_estimate=deleted_item.pomodoro_estimate,
                               pomodoro_completed=deleted_item.pomodoro_completed,
                               itemPriority=itemPriority)
        #deleteObj = DeletedItem(deleted_item)
        deleteObj.save()
        # delete it from items table 
        Item.objects.filter(pk=item_id).delete()
        return redirect('/todolist/')

@login_required(login_url='login/')
def pomodoroTimer(request,id):
    print(id)
    item_id = id
    if item_id :
            # saving the deleted item in deleted table 
        pomodoro_item = Item.objects.get(id=item_id)

    return render(request,"todolist/pomodorotimer.html",{'item':pomodoro_item})

@login_required(login_url='login/')
def updatePomodoroCount(request):
    if request.method == 'POST':
        print("reached pomodoro count")
        item_id = QueryDict(request.body)['id']
        print("update item id",item_id)
        user = request.user
        pomodoro_item = Item.objects.get(id=item_id)
        print(pomodoro_item.pomodoro_completed)
        
        if pomodoro_item:
            count = pomodoro_item.pomodoro_completed  + 1
            print(count)
            Item.objects.filter(pk=item_id).update(pomodoro_completed=count)
            
            itemDict = {'id':item_id, 'pomdoro_completed':count}

            recurItem = RecurringItemStatus(
                user=user,
                item_id=item_id,
                pomodoro_estimated=pomodoro_item.pomodoro_estimate,
                pomodoro_completed=count,
                event_time=datetime.datetime.now()
            )
            recurItem.save()
            return HttpResponse(json.dumps(itemDict), content_type='application/json')           
            

def addUser(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            "form" : form
        }
        return render(request , 'todolist/addUser.html' , context=context)
    else:
        print(request.POST)
        form = UserCreationForm(request.POST)  
        context = {
            "form" : form
        }
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect('todolist:login')
        else:
            return render(request , 'todolist/addUser.html' , context=context)


    '''
    if request.method == "POST":

        customUser = CustomUser(
            username = request.POST.get('username'),
            password = request.POST.get('password'),
            email = request.POST.get('email'),
            profile_name = request.POST.get('profile_name')
        )

        customUser.save()
        return redirect('/todolist/')
    else:
        form = CustomUserForm()

        return render(request, 'todolist/adduser.html', {'form': form})
    '''


def login(request):

    if request.method == 'GET':
        form1 = AuthenticationForm()
        context = {
            "form" : form1
        }
        return render(request , 'todolist/login.html' , context=context )
    else:
        form = AuthenticationForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username , password = password)
            if user is not None:
                loginUser(request , user)
                return redirect('/todolist/')
        else:

            return redirect('todolist:login')

@login_required(login_url='login/')
def signout(request):
    logout(request)
    return redirect('todolist:login')


def checkAndUpdateRecurringTask():
    # get todays date
    today  = datetime.datetime.today().strftime('%Y-%m-%d')
    print("today date",today)
    # Compare it with date in django Sqlite table
    last_date = dateStatusCheck.objects.get(id="1")
    print("last date",last_date)
    # if they mismatch update all the pomodoro completed
    # to zero for recurring tasks and update the value of 
    # table to todays date
    if today != str(last_date):
        # Get all rows which are recurring 
        # update them with "o" for pomodoro completed & 
        # set Status back to not completed
        Item.objects.filter(recurring_task='1').update(pomodoro_completed=0,status=False)
        print("pomodoro values reseted for recurring task")
        dateStatusCheck.objects.filter(id="1").update(today_date=today)

'''
def mappingTelegrambotUser():
    # Get Todays Date
'''
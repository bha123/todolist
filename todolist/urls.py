from django.urls import path

from . import views

app_name = 'todolist'
urlpatterns=[
    path('', views.index, name='index'),
    path('additem/', views.additem , name='additem'),
    path('thanks/', views.thanks, name='thanks'),
    path('ajax/update_item_status', views.update_item_status, name='update_item_status'),
    path('editItem/<int:id>', views.edit_item, name="edit_item"),
    path('deleteItem/<int:id>', views.deleteItem, name="deleteItem"),
    path('pomodorotimer/<int:id>', views.pomodoroTimer, name="pomodoroTimer"),
    path('pomodorotimer/ajax/updatepomodoro', views.updatePomodoroCount, name="updatePomodoroCount"),
    
]
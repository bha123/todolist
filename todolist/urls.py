from django.urls import path

from . import views

app_name = 'todolist'
urlpatterns=[
    path('', views.index, name='index'),
    path('additem/', views.additem , name='additem'),
    path('thanks/', views.thanks, name='thanks'),
    path('ajax/update_item_status', views.update_item_status, name='update_item_status'),
]
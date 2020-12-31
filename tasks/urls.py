from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
  #Categories related
  path('', views.tasks_list, name='tasks_list'),
  path('create/', views.tasks_create, name='tasks_create'),
  path('edit/<int:pk>/', views.tasks_edit, name='tasks_edit'),
  path('delete/<int:pk>/', views.tasks_delete, name='tasks_delete'),

]
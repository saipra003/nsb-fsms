from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import Group

from tasks.forms import TasksForm 
from . models import  XxnfTasks


@login_required
def tasks_list(request, template_name='tasks_list.html'):
    if request.user.is_superuser or request.user.groups.filter(name='parent').exists(): 
        tasks = XxnfTasks.objects.all().order_by('-task_id')
    else:
        tasks = XxnfTasks.objects.filter(owner=request.user).order_by('-task_id')
    data = {}
    data['object_list'] = tasks
    return render(request, template_name, data)

@login_required
def tasks_create(request, template_name='tasks_form.html'):
    form = TasksForm(request.POST or None)
    if form.is_valid():
        tasks = form.save(commit=False)
        #tasks.user = request.user
        tasks.created_by = request.user     #setting the deualt user
        tasks.last_updated_by = request.user    #setting the deualt user
        tasks.save()
        return redirect('tasks:tasks_list')
    return render(request, template_name, {'form':form})

@login_required
def tasks_edit(request, pk, template_name='tasks_form.html'):
    if request.user.is_superuser or request.user.groups.filter(name='parent').exists(): 
        #print(tasks)
        tasks = get_object_or_404(XxnfTasks, pk=pk)
    else:
        tasks = get_object_or_404(XxnfTasks, pk=pk, user=request.user)
    form = TasksForm(request.POST or None, instance=tasks)
    if form.is_valid():
        #form.save()    # coomned to add the below part
        tasks= form.save(commit = False) 
        tasks.last_updated_by = str(request.user)       # converting the username to string from model.instance
        tasks.save()
        return redirect('tasks:tasks_list')
    return render(request, template_name, {'form':form})

@login_required
def tasks_delete(request, pk, template_name='tasks_confirm_delete.html'):
    if request.user.is_superuser or request.user.groups.filter(name='parent').exists(): 
        tasks = get_object_or_404(XxnfTasks, pk=pk)
    else:
        tasks = get_object_or_404(XxnfTasks, pk=pk, user=request.user)
    if request.method=='POST':
        tasks.delete()
        return redirect('tasks:tasks_list')
    return render(request, template_name, {'object':tasks})
from django.shortcuts import render,redirect
from .models import Project, Task
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

# Create your views here.
class Home(ListView):
    model = Project
    template_name = 'app/list.html'

class Create(CreateView):
    model = Project   
    template_name = 'app/create.html'
    fields = ('name','description','duration','image') 
    success_url = 'project/'

class Update(UpdateView):
    model = Project    
    template_name = 'app/create.html'
    fields = ('name','description','duration','image')
    success_url = 'project/'

class Delete(DeleteView):
    model = Project
    template_name = 'app/delete.html'
    success_url = 'project/'

class TaskHome(ListView):
    model = Task
    template_name = 'app/Task_list.html'

class TaskCreate(CreateView):
    model = Task   
    template_name = 'app/task_create.html'
    fields = ('name','description','start_date','end_date') 
    success_url = 'project/'
    
                

class TaskUpdate(UpdateView):
    model = Task
    template_name = 'app/Task_create.html'
    fields = ('name','description','start_date','end_date')
    success_url = 'project/'

class TaskDelete(DeleteView):
    model = Task
    template_name = 'app/Task_delete.html'
    success_url = 'project/'

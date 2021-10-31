from django.shortcuts import render,redirect
from .models import Project, Task
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from .forms import ProjectCreateForm

# Create your views here.
class Home(ListView):
    model = Project
    template_name = 'app/list.html'

class Create(CreateView):
    model = Project   
    template_name = 'app/create.html'
    form_class = ProjectCreateForm
    success_url = '/'
    
    



class Update(UpdateView):
    model = Project    
    template_name = 'app/create.html'
    fields = ('name','description','duration','image')
    success_url = '/'


class Delete(DeleteView):
    model = Project
    template_name = 'app/delete.html'
    success_url = '/'

class Home(ListView):
    model = Task
    template_name = 'app/Task_list.html'

class Create(CreateView):
    model = Task   
    template_name = 'app/task_create.html'
    fields = ('name','description','start_date','end_date') 
    pk_url_kwarg = 'task_id'
    success_url = '<int:project_id>/task/'
    
                

class Update(UpdateView):
    model = Task
    template_name = 'app/Task_create.html'
    fields = ('name','description','start_date','end_date')
    success_url = '/'

class Delete(DeleteView):
    model = Task
    template_name = 'app/Task_delete.html'
    success_url = '/'

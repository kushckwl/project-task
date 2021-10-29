from django.urls import path
from . import views

urlpatterns = [
    path('project/', views.Home.as_view(), name='home'),
    path('project/create/', views.Create.as_view(), name='create'),
    path('project/update/<int:pk>/', views.Update.as_view(), name='update'),
    path('project/delete/<int:pk>/', views.Delete.as_view(), name='delete'),
    path('project/<int:pk>/task/', views.TaskHome.as_view(), name='task_home'),
    path('project/<int:pk>/task/create/', views.TaskCreate.as_view(), name='task_create'),
   
]

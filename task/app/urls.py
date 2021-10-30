from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('create/', views.Create.as_view(), name='create'),
    path('update/<int:pk>/', views.Update.as_view(), name='update'),
    path('detail/<int:pk>/', views.Detail.as_view(), name='detail'),
    path('delete/<int:pk>/', views.Delete.as_view(), name='delete'),
    path('<int:pk>/task/', views.TaskHome.as_view(), name='task_home'),
    path('<int:pk>/task/create/', views.TaskCreate.as_view(), name='task_create'),
   
]

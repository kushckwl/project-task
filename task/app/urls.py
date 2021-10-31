from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('create/', views.Create.as_view(), name='create'),
    path('<int:project_id>/update/', views.Update.as_view(), name='update'),
    path('<int:project_id/delete', views.Delete.as_view(), name='delete'),
    path('<int:project_id>/task/', views.Home.as_view(), name='task_home'),
    path('<int:project_id>/task/create/', views.Create.as_view(), name='task_create'),
    path('<int:project_id>/task/<int:task_id>/update/', views.Update.as_view(), name='task_update'),
    path('<int:project_id>/task/<int:task_id>/delete/', views.Delete.as_view(), name='task_delete'),
   
]

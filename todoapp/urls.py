from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.TaskList.as_view(), name="tasks"),
    #path('task/<int:pk>/', views.TaskDetail.as_view(), name='task_detail'),
    path('create/', views.TaskCreate.as_view(), name='task_create'),
    path('edit-task/<int:pk>/', views.TaskUpdate.as_view(), name='task_edit'),
    path('delete-task/<int:pk>/', views.TaskDelete.as_view(), name='task_delete'),
    path('loginview/', views.TaskLoginView.as_view(), name='login'),
    path('logoutview/', LogoutView.as_view(next_page = "login"), name='logout'),
    path('register/', views.RegistrationView.as_view(), name='register'),
]
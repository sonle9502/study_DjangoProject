from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django import forms
from django.views.decorators.csrf import csrf_exempt

from .models import Task
# Create your views here.

class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'TaskList'  # Name of the variable to use in the template
    paginate_by = 10  # Number of objects to display per page

    @csrf_exempt
    def get_context_data(self, **kwargs):
        # Filter tasks based on the currently logged-in user
        context = super().get_context_data(**kwargs)

        input_searchText_value = self.request.GET.get("text_search")
        input_searchCondition_value = self.request.GET.get("condition_search")

        # Filter data based on the user
        filtered_data = Task.objects.filter(user = self.request.user)

        if input_searchCondition_value == "ID":
            filtered_data = filtered_data.filter(id__icontains = input_searchText_value)
            print(filtered_data)

        elif input_searchCondition_value == "TASK NAME":

            filtered_data = filtered_data.filter(title__icontains = input_searchText_value)
            print(filtered_data)

        #search_data = Task.objects.filter(title_startseith = input_search_value )
        # Add the filtered data to the context
        if input_searchCondition_value is not None:
            context["text_condition_search"] = input_searchCondition_value
        else:
            context["text_condition_search"] = ""

        context['TaskList'] = filtered_data
        if input_searchText_value is not None:
            context['text_search'] = input_searchText_value
        else:
            context["text_search"] = ""
        return context
        

class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields = ["title", "description", "completed"]
    success_url = reverse_lazy('tasks')  # Replace 'success_url_name' with the name of your success URL
    context_object_name = 'TaskCreate'  # Name of the variable to use in the template

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = "__all__" # ["user", "title", ...]
    success_url = reverse_lazy('tasks')  # Replace 'success_url_name' with the name of your success URL

class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')  # Replace 'success_url_name' with the name of your success URL
    context_object_name = 'TaskDelete'  # Name of the variable to use in the template

class TaskLoginView(LoginView):
    fields = "__all__" # ["user", "title", ...]
    template_name = 'todoapp/login.html'  # Path to your template
    
    def get_success_url(self):
        return reverse_lazy('tasks')  

class RegistrationView(FormView):
    template_name = 'todoapp/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('tasks')  # Replace 'login' with your login URL

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)  

from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from .models import User
from django.db import transaction
from django.http import HttpResponse
from .forms import StudentRegisterForm
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.contrib.auth import authenticate, login

#mail

# Create your views here.

# class StudentRegisterView(CreateView):
#     model = User
#     form_class = StudentRegisterForm
#     template_name = 'user/student_register.html'
#     success_url = '/'

#     def form_valid(self, form):
#         # Set the is_manager field to True
#         form.instance.is_student = True
#         return super().form_valid(form)
    
class StudentRegisterView(CreateView):
    model = User
    form_class = StudentRegisterForm
    template_name = 'user/student_register.html'
    success_url = '/'

    def form_valid(self, form):
        # Set the is_manager field to True
        form.instance.is_student = True
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'user/login.html'
    success_url = '/'


    def form_invalid(self, form):
        error_message = 'Invalid username or password'
        return render(self.request, self.template_name, {'error_message': error_message})
    
    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
                error_message = 'Invalid username or password'
                return render(self.request, self.template_name, 'user/login.html', {'error_message': error_message})
    
    def get_redirect_url(self):
        if self.request.user.is_student:
            return reverse('product:index')
        else:
            return '/'


def home(request):
    return HttpResponse("Successfully registered")


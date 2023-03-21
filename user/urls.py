from django.contrib import admin
from django.urls import path, include
from . import views
from .views import StudentRegisterView, UserLoginView, LoginView
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns =  [

    path('studentregister/', StudentRegisterView.as_view(),name='studentregister'),
    path('login/', views.UserLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    # path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('', TemplateView.as_view(template_name='product/index.html'), name='index'),
    
    
    
]

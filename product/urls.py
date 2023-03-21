from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from user.views import home
from . import views
from django.views.generic import TemplateView
app_name = 'product'
urlpatterns = [
    path('index/', views.index, name='index'),    
    

]

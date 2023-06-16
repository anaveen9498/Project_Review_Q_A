"""projectreview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Reviews.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('registration/',registration,name='registration'),
    path('user_login/',user_login,name='user_login'),
    path('user_Logout/',user_Logout,name='user_Logout'),
    path('ask_a_questions/',ask_a_questions,name='ask_a_questions'),
    path('write_answer/',write_answer,name='write_answer'),
    path('question_list/',question_list,name='question_list'),
    path("display_output/",display_output,name="display_output"),
    path('forget_password/',forget_password, name='forget_password'),
    path('change_password/',change_password,name='change_password'),



]   

"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views 

app_name = "main" #for dynamic url names 

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('time/', views.current_date_time, name="time"),
    path('login/', views.login, name="login"),
    path('about/', views.about, name="about"),
    path('review/', views.review, name="review"),
    path('search/', views.SearchPage, name="search"),
    path('course/', views.course, name="course"),

    path('search/SCU/', views.college, name="SCU"),
    path('search/UCSB/', views.college, name="UCSB"),
    path('search/UCB/', views.college, name="UCB"),

    path('search/UCB/addcourse/', views.addCourse, name="addcourse"),
    path('search/UCSB/addcourse/', views.addCourse, name="addcourse"),
    path('search/SCU/addcourse/', views.addCourse, name="addcourse"),

    # path('forms/', views.CourseView, name="forms"),
    # path('review_form_submission/', views.review_form_submission, name="review_form_submission"),
]

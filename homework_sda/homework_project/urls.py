"""homework_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from course.views import hello
from course.models import Technology, Course
from course import views
from course.views import CoursesCreateView

admin.site.register(Technology)
admin.site.register(Course)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello', hello),
    path('', views.CoursesView.as_view()),
    path('courses/', views.CoursesView.as_view()),
    path('course/create',CoursesCreateView.as_view(), name = 'course_create')

]

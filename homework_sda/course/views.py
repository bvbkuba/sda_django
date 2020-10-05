from django.shortcuts import render
from django.http import HttpResponse
from course.models import Course
from django.views.generic import ListView, FormView
from course.models import Course
from course.forms import CourseForm


def hello(request):
    return HttpResponse("Hey space")

# def courses(request):
#     return render(
#         request, template_name = 'courses.html', context= {'courses': Course.objects.all()}
#     )

class CoursesView(ListView):
    template_name = 'courses.html'
    model = Course
    ordering = ['price']

class CoursesCreateView(FormView):
    template_name = 'forms.html'
    form_class = CourseForm
    success_url = '/courses/'


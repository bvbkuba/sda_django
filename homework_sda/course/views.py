from django.shortcuts import render
from django.http import HttpResponse
from course.models import Course
from django.views.generic import ListView

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
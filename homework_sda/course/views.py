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

    def form_valid(self,form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data()
        Course.objects.create(
            title = cleaned_data('title'),
            technology_id = cleaned_data('technology_id'),
            description = cleaned_data('description'),
            starts = cleaned_data('starts'),
            finished = cleaned_data('finished'),
            max_atendees_count = cleaned_data('max_atendes_count'),
            price = cleaned_data('price'),
            remote = cleaned_data('remote')

        )






# from course.mixins import TitleMixin

# class SubmittableLoginView(TitleMixin,SubmittableLoginView):
#     title = 'Login'
#     form_class = SubmittableAuthenticationForm
#     template_name = 'form.html'

# class SubmittablePasswordChangeView(TitleMixin,PasswordChangeView):
#     title = 'Password Change'
#     form_class = SubmittablePasswordChangeForm
#     template_name = 'form.html'
#     success_url = reverse_lazy('index')

# class SignUpView(TitleMixin, CreateView):
#     title = 'Sin Up'
#     template_name = 'form.html'
#     form_class = SignUpForm
#     success_url = reverse_lazy('index')
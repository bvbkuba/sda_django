from django import forms
from course.models import Technology
from datetime import datetime


def future_date(date_value):
    if date_value < datetime.today().date():
        raise ValueError(
            'Please, write correct datetime. Course can start only in future')
# def end_date(data_value):
#     if data_value <= CourseForm.starts():
#         raise ValueError(
#             'Please, write correct datetime. Date of start course cannot be higher than finished date')



class CourseForm(forms.Form):
    title = forms.CharField(max_length=100)
    technology_id = forms.ModelChoiceField(queryset=Technology.objects)
    description = forms.CharField(widget=forms.Textarea, required=False)
    starts = forms.DateField(validators=[future_date])
    # finished = forms.DateField(validators=[end_date], required=False)
    finished = forms.DateField(required=False)
    max_atendees_count = forms.IntegerField(min_value=5, max_value=10)
    price = forms.FloatField(min_value=0.00)
    remote = forms.CheckboxInput()

from django import forms
from course.models import Technology
from datetime import datetime
from django.core.exceptions import ValidationError
from datetime import date


def future_date(date_value):
    if date_value < datetime.today().date():
        raise ValueError(
            'Please, write correct datetime. Course can start only in future')
# def end_date(data_value):
#     if data_value <= CourseForm.starts():
#         raise ValueError(
#             'Please, write correct datetime. Date of start course cannot be higher than finished date')


class FutureDateField(forms.DateField):
    def validate(self, value):
        super().validate(value)
        if value < datetime.today().date():
            raise ValidationError('Only future dates allowed here')

    def clean(self, value):
        result = super().clean(value)
        return date(year= result.year, month = result.month, day = 1)


class AfterStartDateField(forms.DateField):
    def validate(self, value):
        super().validate(value)
        if value <= datetime.today().date():
            raise ValidationError('Only dates higher than start course allowed here')


class CourseForm(forms.Form):
    title = forms.CharField(max_length=100)
    technology_id = forms.ModelChoiceField(queryset=Technology.objects)
    description = forms.CharField(widget=forms.Textarea, required=False)
    # starts = forms.DateField(validators=[future_date])
    starts = FutureDateField()
    # finished = forms.DateField(validators=[end_date], required=False)
    finished = AfterStartDateField(required=False)
    max_atendees_count = forms.IntegerField(min_value=5, max_value=10)
    price = forms.FloatField(min_value=0.00)
    remote = forms.CheckboxInput()

from django.forms import ModelForm
from django import forms
from .models import WorkDay

class WorkDayForm(ModelForm):

    work_start = forms.DateTimeField(input_formats=['%d.%m.%Y %H:%M'],
        widget = forms.DateTimeInput(
            format ='%d.%m.%Y %H:%M'))
    work_end = forms.DateTimeField(input_formats=['%d.%m.%Y %H:%M'],
        widget = forms.DateTimeInput(
            format ='%d.%m.%Y %H:%M'))

    class Meta:
        model = WorkDay
        fields = [
            'work_start',
            'work_end',
            'bus_number',
            'start_mileage',
            'end_mileage',
        ]
        
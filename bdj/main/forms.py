
from django import forms
from .models import WorkDay

class WorkDayForm(forms.ModelForm):
    class Meta:
        model = WorkDay
        fields = [
            'work_start',
            'work_end',
            'bus_number',
            'start_mileage',
            'end_mileage',
        ]

        widgets = {
            'work_start': forms.DateTimeInput(format ='%d.%m.%Y %H:%M', attrs={'class': 'form-control'}),
            'work_end': forms.DateTimeInput(format ='%d.%m.%Y %H:%M', attrs={'class': 'form-control'}),
            'bus_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'start_mileage': forms.NumberInput(attrs={'class': 'form-control'}),
            'end_mileage': forms.NumberInput(attrs={'class': 'form-control'}),

        }
        
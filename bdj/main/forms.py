
from django import forms
from .models import WorkDay
from django.core.exceptions import ValidationError


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
            'work_start': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'work_end': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'bus_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'start_mileage': forms.NumberInput(attrs={'class': 'form-control'}),
            'end_mileage': forms.NumberInput(attrs={'class': 'form-control'}),

        }
    
    def clean(self):
 
        super(WorkDayForm, self).clean()
        work_start = self.cleaned_data['work_start']
        work_end = self.cleaned_data['work_end']
        start_mileage = self.cleaned_data['start_mileage']
        end_mileage = self.cleaned_data['end_mileage']

        if work_start > work_end:
            self._errors['Rozpoczęcie pracy'] = self.error_class([
                'Rozpoczęcie pracy nie może być po jego zakończeniu.'])
        if end_mileage < start_mileage:
            self._errors['Licznik Końcowy'] = self.error_class([
                'Licznik końcowy nie może być mniejszy, niż początkowy.'])
            
 
        return self.cleaned_data

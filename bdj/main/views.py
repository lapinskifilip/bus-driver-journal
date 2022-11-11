from django.shortcuts import render
from .models import WorkDay


def homepage(request):
    return render(request, "main/index.html", context={})


def workdays(request):
    workdays = WorkDay.objects.all()
    context = {"workdays": workdays}

    return render(request, "main/workdays/list.html", context)


def workdays_details(request, workdays_id):
    workdays = WorkDay.objects.get(pk=workdays_id)
    context = {"workdays_details": workdays}

    return render(request, "main/workdays/details.html", context)

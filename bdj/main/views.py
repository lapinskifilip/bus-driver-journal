from django.shortcuts import render, redirect
from django.contrib import messages
from .models import WorkDay


def homepage(request):
    return render(request, "main/index.html", context={})


def weekday_schedules(request):
    return render(request, "main/schedules/weekday.html", context={})


def saturday_schedules(request):
    return render(request, "main/schedules/saturday.html", context={})


def sunday_schedules(request):
    return render(request, "main/schedules/sunday.html", context={})


def workdays_list(request):
    workdays_by_author = WorkDay.objects.filter(author=request.user)
    context = {"workdays_by_author": workdays_by_author}

    return render(request, "main/workdays/list.html", context)


def workdays_details(request, workdays_id):
    workdays = WorkDay.objects.get(pk=workdays_id)
    context = {"workdays_details": workdays}
    if not workdays.author.id == request.user.id:
        messages.error(
            request,
            "Nie można uzyskać podglądu do dnia innego kierowcy. Zostałeś przekierowany na stronę główną.",
        )
        return redirect("/")

    return render(request, "main/workdays/details.html", context)

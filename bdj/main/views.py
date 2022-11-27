from django.shortcuts import render, redirect
from django.contrib import messages
from .models import WorkDay
from .forms import WorkDayForm


def homepage(request):
    return render(request, "main/index.html", context={})


def weekday_schedules(request):
    return render(request, "main/schedules/weekday.html", context={})


def saturday_schedules(request):
    return render(request, "main/schedules/saturday.html", context={})


def sunday_schedules(request):
    return render(request, "main/schedules/sunday.html", context={})

def contact(request):
    return render(request, "main/contact.html", context={})

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


def workday_add(request):

    form = WorkDayForm()
    if request.method == "POST":
        form = WorkDayForm(request.POST)
        if form.is_valid():
            workday = form.save(commit=False)
            workday.author = request.user
            workday.save()
            messages.success(request, "Pomyślnie dodano nowy dzień pracy")
            return redirect("/")

    context = {'form': form}
    return render(request, "main/workdays/add_workday.html", context)

def workday_edit(request, workdays_id):
    workday = WorkDay.objects.get(id=workdays_id)
    form = WorkDayForm(instance=workday)

    if request.method == "POST":
        form = WorkDayForm(request.POST, instance=workday)
        if form.is_valid():
            workday = form.save(commit=False)
            workday.author = request.user
            workday.save()
            messages.success(request, "Pomyślnie zmodyfikowano dzień pracy")
            return redirect("/")

    context = {'form': form}
    return render(request, "main/workdays/add_workday.html", context)

def workday_delete(request, workdays_id):
    workday = WorkDay.objects.get(id=workdays_id)
    if request.method == "POST":
        workday.delete()
        messages.success(request, "Pomyślnie usunięto dzień pracy")
        return redirect("/")
    context = {'workday': workday}
    return render(request, "main/workdays/delete_workday.html", context)

    
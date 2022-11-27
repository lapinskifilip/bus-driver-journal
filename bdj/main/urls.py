from django.urls import path, include
from .views import (
    homepage,
    weekday_schedules,
    saturday_schedules,
    sunday_schedules,
    contact,
    workdays_list,
    workdays_details,
    workday_edit,
    workday_delete,
    workday_add,
)

app_name = "main"
urlpatterns = [
    path("", homepage, name="homepage"),
    path("schedules/weekday/", weekday_schedules, name="weekday_schedules"),
    path("schedules/saturday/", saturday_schedules, name="saturday_schedules"),
    path("schedules/sunday/", sunday_schedules, name="sunday_schedules"),
    path("contact/", contact, name="contact"),
    path("workdays/", workdays_list, name="workdays_list"),
    path("workdays/<int:workdays_id>", workdays_details, name="workdays_details"),
    path("workdays/<int:workdays_id>/edit", workday_edit, name="workday_edit"),
    path("workdays/<int:workdays_id>/delete", workday_delete, name="workday_delete"),
    path("workdays/add/", workday_add, name="workday_add")
]

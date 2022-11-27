from django.urls import path, include
from .views import (
    homepage,
    weekday_schedules,
    saturday_schedules,
    sunday_schedules,
    workdays_list,
    workdays_details,
    workday_add,
)

app_name = "main"
urlpatterns = [
    path("", homepage, name="homepage"),
    path("schedules/weekday/", weekday_schedules, name="weekday_schedules"),
    path("schedules/saturday/", saturday_schedules, name="saturday_schedules"),
    path("schedules/sunday/", sunday_schedules, name="sunday_schedules"),
    path("workdays/", workdays_list, name="workdays_list"),
    path("workdays/<int:workdays_id>", workdays_details, name="workdays_details"),
    path("workdays/add/", workday_add, name="workday_add")
]

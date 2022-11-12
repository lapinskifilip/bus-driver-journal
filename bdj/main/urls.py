from django.urls import path, include
from .views import (
    homepage,
    weekday_schedules,
    saturday_schedules,
    sunday_schedules,
    workdays,
    workdays_details,
)

app_name = "main"
urlpatterns = [
    path("", homepage, name="homepage"),
    path("schedules/weekday/", weekday_schedules, name="weekday_schedules"),
    path("schedules/saturday/", saturday_schedules, name="saturday_schedules"),
    path("schedules/sunday/", sunday_schedules, name="sunday_schedules"),
    path("workdays/", workdays, name="workdays"),
    path("workdays/<int:workdays_id>", workdays_details, name="workdays_details"),
]

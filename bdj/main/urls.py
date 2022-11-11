from django.urls import path, include
from .views import homepage, workdays, workdays_details

app_name = "main"
urlpatterns = [
    path("", homepage, name="homepage"),
    path("workdays/", workdays, name="workdays"),
    path("workdays/<int:workdays_id>", workdays_details, name="workdays_details"),
]

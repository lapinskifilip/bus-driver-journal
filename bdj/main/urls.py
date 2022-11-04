from django.urls import path, include
from .views import homepage

app_name = "main"
urlpatterns = [
    path('', homepage, name="homepage"),
]
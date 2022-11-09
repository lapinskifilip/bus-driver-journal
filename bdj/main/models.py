from django.db import models


class DriverProfile(models.Model):
    driver = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    work_number = models.SmallIntegerField()


class WorkDay(models.Model):
    work_date = models.DateField(auto_now_add=True)
    work_start = models.TimeField()
    work_end = models.TimeField()

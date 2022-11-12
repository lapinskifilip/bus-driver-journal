from django.db import models


class DriverProfile(models.Model):
    driver = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    work_number = models.SmallIntegerField()


class WorkDay(models.Model):

    work_date = models.DateField(auto_now_add=True)
    work_start = models.DateTimeField()
    work_end = models.DateTimeField()

    bus_number = models.CharField(max_length=20, default=0)
    start_mileage = models.IntegerField(default=0)
    end_mileage = models.IntegerField(default=0)

    @property
    def work_hours(self):
        return self.work_end - self.work_start

    @property
    def total_mileage(self):
        return self.end_mileage - self.start_mileage

    def __str__(self) -> str:
        return f"{self.work_hours}"


class Schedule(models.Model):
    title = models.CharField(max_length=3)

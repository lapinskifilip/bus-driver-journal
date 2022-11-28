from django.db import models


class DriverProfile(models.Model):
    driver = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    work_number = models.SmallIntegerField()


class WorkDay(models.Model):

    work_date = models.DateField(auto_now_add=True)
    work_start = models.DateTimeField()
    work_end = models.DateTimeField()
    bus = models.ForeignKey("Bus", null=True, default=None, on_delete=models.CASCADE, related_name="bus_number")
    start_mileage = models.IntegerField(default=0)
    end_mileage = models.IntegerField(default=0)

    author = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="workdays"
    )

    @property
    def work_hours(self):
        return self.work_end - self.work_start

    @property
    def total_mileage(self):
        return self.end_mileage - self.start_mileage

    def __str__(self) -> str:
        return f"{self.work_hours}"


class Bus(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    registration_number = models.CharField(max_length=10)
    total_odometer = models.IntegerField()

    def __str__(self):
        return f"[{self.number}] [{self.registration_number}]"


class Schedule(models.Model):
    title = models.CharField(max_length=3)

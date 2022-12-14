from django.contrib import admin
from .models import DriverProfile, WorkDay, Schedule


@admin.register(DriverProfile)
class DriverProfileAdmin(admin.ModelAdmin):
    list_display = [
        "work_number",
    ]


@admin.register(WorkDay)
class WorkDayAdmin(admin.ModelAdmin):
    list_display = [
        "work_date",
        "work_start",
        "work_end",
        "work_hours",
        "bus_number",
        "start_mileage",
        "end_mileage",
        "total_mileage",
    ]


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin
from .models import DriverProfile, WorkDay, Bus, Schedule


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
        "bus",
        "start_mileage",
        "end_mileage",
        "total_mileage",
    ]

@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "number",
        "registration_number",
        "total_odometer"
    ]

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    pass

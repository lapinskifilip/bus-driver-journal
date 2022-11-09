from django.contrib import admin
from .models import DriverProfile, WorkDay


@admin.register(DriverProfile)
class DriverProfileAdmin(admin.ModelAdmin):
    list_display = ["driver", "work_number", "first_name", "last_name"]


@admin.register(WorkDay)
class WorkDayAdmin(admin.ModelAdmin):
    pass

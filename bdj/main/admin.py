from django.contrib import admin
from .models import Driver, WorkDay


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkDay)
class WorkDayAdmin(admin.ModelAdmin):
    pass

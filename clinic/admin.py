from django.contrib import admin
from .models import Clinic, Doctor


@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'surname',
    )

from django.contrib import admin
from .models import Clinic, Doctor


@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'surname',
        'email'
    )
    prepopulated_fields = {'slug': ('name', )}
    search_fields = ('name',)
    list_filter = ('name', 'created')

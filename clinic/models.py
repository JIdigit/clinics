from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Clinic(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.IntegerField()

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class Doctor(models.Model):
    profile = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    clinic = models.ForeignKey(Clinic, related_name='clinic', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


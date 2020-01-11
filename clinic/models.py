from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone


class Clinic(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    image_height = models.IntegerField(default=0)
    image_width = models.IntegerField(default=0)
    image = models.ImageField(upload_to='clinics/%Y/%m/%d', max_length=200, blank=True,
                              height_field='image_height', width_field='image_width')
    phone_number = models.IntegerField()

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class Doctor(models.Model):
    # username = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    username = models.CharField(max_length=100)
    clinic = models.ForeignKey(Clinic, related_name='clinic', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, default=None)
    email = models.EmailField(default=None)
    proffesion = models.CharField(max_length=100)
    image_height = models.IntegerField(default=50)
    image_width = models.IntegerField(default=70)
    image = models.ImageField(upload_to='doctors/%Y/%m/%d', max_length=200, blank=True,
                              height_field='image_height', width_field='image_width')
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


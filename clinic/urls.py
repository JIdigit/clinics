from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', doctor_login, name='login'),
    path('logout/', doctor_logout, name='logout'),
    path('register/', register, name='register'),
    path('clinics_list/', ClinicsListView.as_view(), name='clinics_list_view'),
    path('doctor_list/', DoctorListView.as_view(), name='doctor_list'),
    path('test/', test, name='test')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.shortcuts import render, HttpResponse
from .forms import DoctorLoginForm, DoctorRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView, ListView
from .models import Doctor, Clinic
from django.contrib.auth.models import User
import random
import string


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


class HomePageView(TemplateView):
    template_name = 'home.html'


def doctor_login(request):
    if request.method == 'POST':
        form = DoctorLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'home.html', {'user': user})
            else:
                return HttpResponse(' NO SUCH ACCOUNT')

    else:
        form = DoctorLoginForm()
    return render(request, 'account/login.html', {'form': form})


def doctor_logout(request):
    logout(request)
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        user_form = DoctorRegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            username = user_form.cleaned_data['username']
            name = user_form.cleaned_data['name']
            surname = user_form.cleaned_data['surname']
            clinic_id = user_form.cleaned_data['clinic']
            # clinic = user_form.cleaned_data['clinic']
            # new_user.set_password(user_form.cleaned_data['password'])
            # new_user.save()
            login(request, new_user)
            Doctor.objects.create(name=name, surname=surname, slug=rand_slug(), clinic_id=clinic_id)
            User.objects.create(username=username,password=user_form.password, first_name=name, last_name=surname, email=None).save()
                                  # clinic_id=clinic, slug=rand_slug()).save()
            return render(request,
                          'home.html',
                          {'new_user': new_user})
    else:
        user_form = DoctorRegisterForm()
    return render(request,
                  'account/register.html',
                  {'form': user_form})


class ClinicsListView(ListView):
    model = Clinic
    template_name = 'clinics.html'
    context_object_name = 'clinics'


class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctor_list.html'
    context_object_name = 'doctors'


def test(request):
    return render(request, 'Doctors.html')




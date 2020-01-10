from django.shortcuts import render, HttpResponse
from .forms import DoctorLoginForm, DoctorRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView, ListView
from .models import Doctor


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
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            try:
                Doctor.objects.create(user=new_user)
            except:
                return render(request,
                              'home.html',
                              {'new_user': new_user})
    else:
        user_form = DoctorRegisterForm()
    return render(request,
                  'account/register.html',
                  {'form': user_form})




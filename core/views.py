import json

from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from .models import SolarPanels, InvertersModel, BatteryModel


def calculator(request):
    return render(request, 'wasd.html')


def home(request):
    return render(request, 'home.html')


def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Ulanyjy alnan!')
                return redirect('sign-up')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                return redirect('/')
        else:
            messages.info(request, 'Gizlin sözüňiz deň gelenok!')
            return redirect('sign-up')
    else:
        return render(request, 'sign_up.html')


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Maglumatlaryňyz ýalňyş girizilen!')
            return redirect('signin')

    else:
        return render(request, 'sign_in.html')


@login_required(login_url='sign-in')
def sign_out(request):
    auth.logout(request)
    return redirect('home')


@login_required(login_url='sign-in')
def calculated_panels(request):
    return render(request, 'calculated_panels.html')


def fetch_solar_components(request):
    try:
        # Fetch all components in parallel
        panels = SolarPanels.objects.all().values()
        inverters = InvertersModel.objects.all().values()
        batteries = BatteryModel.objects.all().values()
        data = {
            'panels': list(panels),
            'inverters': list(inverters),
            'batteries': list(batteries)
        }
        return JsonResponse(data)

        # return HttpResponse(data, content_type='application/json')

    except Exception as e:
        return HttpResponse(e, content_type='application/json',)

from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import House, Travel


# custom required decorator
def login_required_decorator(func):
    return login_required(func, login_url='account:login')


# creating user
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


# rent house functions
@login_required_decorator
def house(request):
    houses = House.objects.all()
    courtyards = House.objects.filter(rent_house='courtyard')
    print(houses)

    context = {
        "houses": houses,
        "courtyards": courtyards,
    }
    return render(request, 'house/house.html', context)


@login_required_decorator
def courtyard(request):
    courtyards = House.objects.filter(rent_house='courtyard')

    context = {
        "courtyards": courtyards,
    }
    return render(request, 'house/courtyard.html', context)


@login_required_decorator
def apartment(request):
    apartments = House.objects.filter(rent_house='apartment')

    context = {
        "apartments": apartments,
    }
    return render(request, 'house/apartment.html', context)


@login_required_decorator
def contract(request):
    contracts = House.objects.filter(rent_contract='contract')

    context = {
        "contracts": contracts,
    }
    return render(request, 'house/contract.html', context)


@login_required_decorator
def nocontract(request):
    nocontracts = House.objects.filter(rent_contract='nocontract')

    context = {
        "nocontracts": nocontracts,
    }
    return render(request, 'house/nocontract.html', context)


# TRAVEL functions
@login_required_decorator
def travel(request):
    travels = Travel.objects.all()

    context = {
        "travels": travels,
    }
    return render(request, 'travel/travel.html', context)


@login_required_decorator
def trip(request):
    trips = Travel.objects.filter(name='trip')

    context = {
        "trips": trips,
    }
    return render(request, 'travel/trip.html', context)


@login_required_decorator
def library(request):
    libraries = Travel.objects.filter(name='library')

    context = {
        "libraries": libraries,
    }
    return render(request, 'travel/library.html', context)


@login_required_decorator
def food(request):
    foods = Travel.objects.filter(name='food')

    context = {
        "foods": foods,
    }
    return render(request, 'travel/food.html', context)

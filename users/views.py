from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from .models import User, House


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


def house(request):
    houses = House.objects.all()
    courtyards = House.objects.filter(rent_house='courtyard')
    print(houses)

    context = {
        "houses": houses,
        "courtyards": courtyards,
    }
    return render(request, 'house/house.html', context)


def courtyard(request):
    courtyards = House.objects.filter(rent_house='courtyard')

    context = {
        "courtyards": courtyards,
    }
    return render(request, 'house/courtyard.html', context)


def apartment(request):
    apartments = House.objects.filter(rent_house='apartment')

    context = {
        "apartments": apartments,
    }
    return render(request, 'house/apartment.html', context)


def contract(request):
    contracts = House.objects.filter(rent_contract='contract')

    context = {
        "contracts": contracts,
    }
    return render(request, 'house/contract.html', context)


def nocontract(request):
    nocontracts = House.objects.filter(rent_contract='nocontract')

    context = {
        "nocontracts": nocontracts,
    }
    return render(request, 'house/nocontract.html', context)

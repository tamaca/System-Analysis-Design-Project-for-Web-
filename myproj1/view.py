from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {}
    context['key'] = "value"
    return render(request, 'index.html', context)

def login(request):
    context = {}
    context['key'] = "value"
    return render(request, 'login.html', context)

def register(request):
    context = {}
    context['key'] = "value"
    return render(request, 'register.html', context)

def hospitals(request):
    context = {}
    context['key'] = "value"
    return render(request, 'hospitals.html', context)

def orders(request):
    context = {}
    context['key'] = "value"
    return render(request, 'orders.html', context)

def checkout(request):
    context = {}
    context['key'] = "value"
    return render(request, 'checkout.html', context)

def contact(request):
    context = {}
    context['key'] = "value"
    return render(request, 'contact.html', context)
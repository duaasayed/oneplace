from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import User
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from pprint import pprint

@require_http_methods(['POST'])
def save_user(request):
    data = request.POST
    pprint(request.POST)
    if data['password1'] != data['password2']:
        return JsonResponse({'status': 422})

    user = User.objects.create_user(
        email=data['email'],
        password=data['password1'],
        first_name=data['first_name'],
        last_name=data['last_name']
    )
    
    return JsonResponse({'status': 200})


@require_http_methods(['POST'])
def login_view(request):
    data = request.POST
    user = authenticate(email=data['email'], password=data['password'])
    if not user:
        return JsonResponse({'status': 422})

    login(request, user)
    return redirect('/')
    

@require_http_methods(['POST'])
def logout_view(request):
    logout(request)
    return redirect('/')

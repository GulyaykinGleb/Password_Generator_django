from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def me(request):
    return render(request, 'generator/me.html')

def password(request):
    thepassword = ''
    characters = list('abcdefghiz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFG'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    if request.GET.get('special'):
        characters.extend(list('!@#$.,/'))
    length = int(request.GET.get('length', 12))

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword, 'password1': request.POST.get('special')})

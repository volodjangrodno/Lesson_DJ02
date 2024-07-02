from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def clicker(request):
    return render(request, 'main/clicker.html')

def community(request):
    return render(request, 'main/community.html')

def contact(request):
    return render(request, 'main/contact.html')

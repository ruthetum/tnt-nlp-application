from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Mynote
import re, random, sys, os
import pdfkit
# from .models import Profile, Story, Region #적용할 모델들


def home(request):
    return render(request, 'intro.html')

def aboutPage(request):
    return render(request, 'about.html')

def functionPage(request):
    return render(request, 'function.html')

def streamingPage(request):
    return render(request, 'streaming.html')

def cornellPage(request):
    mynotes = Mynote.objects.filter(auther="jungmin").first()
    return render(request, 'cornell.html', {'mynotes': mynotes})

def cnDetail(request):
    return render(request, 'cornellDetail.html')

def update(request):
    if request.method == "POST":
        input_title = request.POST['title']
        input_k1 = request.POST['k1']
        input_k2 = request.POST['k2']
        input_k3 = request.POST['k3']
        input_k4 = request.POST['k4']
        input_k5 = request.POST['k5']
        input_note = request.POST['note']
        input_summary = request.POST['summary']

        Mynote.objects.get(auther="jungmin")



    return render(request, 'cornell.html')

def resultPage(request):
    return render(request, 'result.html')

def creditPage(request):
    return render(request, 'credit.html')


    

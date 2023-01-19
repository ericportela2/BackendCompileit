from django.shortcuts import render
from django.urls import reverse

# Create your views here.



def index(response):
    return render(response, "main_menu/index.html")

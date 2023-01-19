from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django import forms

import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate("backendcompileitcase-firebase-adminsdk-penpe-db655dd824.json")
firebase_admin.initialize_app(cred)

class LoginForm(forms.Form):

    username = forms.EmailField(label="Username") #'username' är nyckeln i dictionaryn som returneras av request.POST
    password = forms.CharField(widget=forms.PasswordInput(), min_length=6)


def createUser(email, pswd, request):

        try: #Användaren lyckades att skapas!
            user = auth.create_user(email = email, password = pswd)
            
            print("User created successfully!")

            return HttpResponseRedirect(reverse("login:"))

        except auth.EmailAlreadyExistsError: #Användaren finns redan :(
            print("User already exists!")

            return HttpResponseRedirect(reverse("login:loginFailed")) #reverse tar reda på url av login app:en och använder den url för att redirecta


# Create your views here.
def index(request):

    if request.method == "POST" :
        form = LoginForm(request.POST)


        email = request.POST["username"]
        password = request.POST["password"]
       
        try:
            user = auth.create_user(email = email, password = password)
            
            print("User created successfully!")

            return HttpResponseRedirect(reverse("login:loginSuccessful")) #reverse tar reda på url av login app:en och använder den url för att redirecta

        except auth.EmailAlreadyExistsError:
            print("User already exists!")

            return HttpResponseRedirect(reverse("login:loginFailed"))
        

    return render(request, "login/index.html", {
        "form": LoginForm()
    })


def failedLogin(request):
    return render(request, "login/loginFailed.html")

def successfulLogin(request):
    return render(request, "login/successfulLogin.html")

from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

from django import forms

import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

import json
import requests

# Create your views here.

apiKey = "AIzaSyBY0jEY2lkfRwd_ZT2x9dtbbgffdCHHAEk" #DÅLIGT val (I KNOW), men fanns ingen annan möjlighet med Firebase...
e_mail_reset = []

class LoginForm(forms.Form):

    username = forms.EmailField(label="Username") #'username' will be key in dictionary that is returned by request.POST
    password = forms.CharField(widget=forms.PasswordInput(), min_length=6)


# Se docs:en om att logga in med email + lösen genom HTTP request. Länk nedan.
# https://firebase.google.com/docs/reference/rest/auth#section-sign-in-email-password
def sign_in(email, password):
    request_ref = f"https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={apiKey}"
    headers = {"content-type": "application/json; charset=UTF-8"}
    data = json.dumps({"email": email, "password": password, "returnSecureToken": True})
    request_object = requests.post(request_ref, headers=headers, data=data)
    return request_object.json()


def index(request):

    if request.method == "POST":

        form = LoginForm(request.POST)

        e_mail_reset.clear()

        email = request.POST["username"]
        password = request.POST["password"]
        e_mail_reset.append(email)

        response = (sign_in(email=email, password=password))

        print(response)

        try:
            if response['registered'] == True:
                return HttpResponseRedirect(reverse("create:sucessfulLogin"))


        except KeyError:

            print(response['error']['message'])

            return render(request, "create/fail.html", {
                "response": response['error']['message'] 
            })



    return render(request, "create/index.html", {
        "form": LoginForm()
    })


def sucessfulLogin(request):

    return render(request, "create/sucess.html")


def failedLogin(request):

    return render(request, "create/sucess.html")


def forgotMyPassword(request):
    if request.method == "POST":
        link = auth.generate_password_reset_link(email=e_mail_reset[0])
        print(e_mail_reset[0])
        return render(request, "create/reset.html", {
            "email": e_mail_reset[0], 
            "link": link
        })

    else:
        return None

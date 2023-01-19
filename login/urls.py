from django.urls import path
from . import views

#EXTREMT VIKTIG GLOBAL VARIABEL!!!!
#Glöm INTE att man i [projektets urls.py] måste lägga till [path till urls.py i apparna]!!!!!!!
#Märk väl skillnad mellan projekt och app!!!

app_name = "login" #Viktigt som fan för att kunna kalla på reverse(login:index) t.ex. eller i html: {% url 'login:failedLogin' %}

urlpatterns = [

    path("", views.index, name="index"),
    path("fail", views.failedLogin, name = "loginFailed"),
    path("sucess", views.successfulLogin, name = "loginSuccessful")

    ]
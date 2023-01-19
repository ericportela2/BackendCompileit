from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django import forms

import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth


# Create your views here.

searchResults = []

class SearchForm(forms.Form):

    search = forms.CharField()



def index(request):

    if request.method == "POST" :

        searchResults.clear()

        searchWord = request.POST["search"]

        for user in auth.list_users().iterate_all():
            if (searchWord in user.email):
                searchResults.append(user.email)


        return HttpResponseRedirect(reverse("search:results"))

    return render(request, "search/index.html", {
        "form": SearchForm()
    })


def findResults(request):

    data = {
        "searchResults": searchResults,
        "count": len(searchResults)
    }

    return render(request, "search/results.html", data)


# En separat metod som söker igenom den returnerade resultatlistan med ex. binärsökning (O(logn)) skulle vara fördelaktigt vid stora mängder användare!!!

# Givet case:ts förutsättningar och det faktum att databasen är tom implementerades inte en sådan lösning.
# Borde gå fort att implementera en metod som mha binärsökning letar reda på rätt användare.

# Man skulle exempelvis kunna i samband med att man "retriev:ar" listan med användare (O(n)) skapa en separat lista som representerar 
# användarnas strängar som tal, sortera den med antingen en inbyggd sorteringsalgo eller ex. mergesort.
# Därefter kan binärsökning köras.

# Efter att snabbt kikat igenom Firebase docs verkar det som att det enda sättet är att iterera sig genom hela databasen i en batch
# om 1000 datapunkter per gång.
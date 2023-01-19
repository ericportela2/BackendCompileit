from django.urls import path
from . import views

#EXTREMT VIKTIG GLOBAL VARIABEL!!!!!!!
app_name = "main_menu"

urlpatterns = [
        
        path("", views.index, name = "index")

]
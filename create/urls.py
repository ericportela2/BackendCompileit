from django.urls import path
from .import views

app_name = "create"

urlpatterns = [
        
        path("", views.index, name = "index"),
        path("sucessful", views.sucessfulLogin, name = "sucessfulLogin"),
        path("fail", views.failedLogin, name = "failedLogin"),
        path("forgotmypassword", views.forgotMyPassword, name = "forgotPswd")
]
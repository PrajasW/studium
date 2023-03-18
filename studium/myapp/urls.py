from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.open_home),
    path('login',views.open_login),
    path('signup',views.open_signup),
    path('user',views.user),
    path('aboutus',views.open_aboutus),
]

from django.shortcuts import render

# Create your views here.
def open_home(request):
    return render(request,'home.html')

def open_login(request):
    return render(request,'login.html')

def open_signup(request):
    return render(request,'signup.html')

def user(request):
    return render(request,'user.html')

def open_aboutus(request):
    return render(request,'aboutus.html')
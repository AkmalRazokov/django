from django.shortcuts import render, HttpResponse, redirect
from .models import CustomUser
from django.contrib.auth import login, logout, authenticate

def register_view(request):
    if request.method == "GET":
        return render(request, "register.html")
    elif request.method == "POST":
        email = request.POST.get('email', False)
        password = request.POST.get('password', False)
        confirm_password = request.POST.get('confirm_password', False)
        if password!=confirm_password:
            return HttpResponse('Check password')
        user = CustomUser.objects.create_user(email = email, password=password)
        return redirect('login')
        


def login_view(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        email = request.POST.get('email', False)
        password = request.POST.get('password', False)
        if not email or not password:
            return HttpResponse('Check password')
        user = authenticate(email = email, password = password)
        CustomUser.objects.filter(id = user).first()
        email = email,



        

from django.shortcuts import render, HttpResponse, redirect
from .models import CustomUser, ConfirmationToken, PasswordResetToken
from django.contrib.auth import login, logout, authenticate
from .helpers import send_confirmation_token
from django.conf import settings
from django.core.mail import send_mail

def register_view(request):
    if request.method == "GET":
        return render(request, "register.html")
    elif request.method == "POST":
        email = request.POST.get('email', False)
        password = request.POST.get('password', False)
        confirm_password = request.POST.get('confirm_password', False)
        first_name = request.POST.get('first_name', False)
        last_name = request.POST.get('last_name', False)
        if not email or not password or not confirm_password or not first_name or not last_name:
            return HttpResponse('Please fill all required fields.')
        if password!=confirm_password:
            return HttpResponse('Check password')
        if CustomUser.objects.filter(email=email).exists():
            return HttpResponse("Пользователь с таким email уже существует.")
        user = CustomUser.objects.create_user(
            email = email,
            password=password,
            first_name=first_name,
            last_name=last_name
            )
        user.is_active = False
        user.save()
        confirm_email_object = ConfirmationToken.objects.create(user = user)
        token = confirm_email_object.token
        res = send_confirmation_token(email, token)
        if res["is_sent"]:
            print(res["message"])
            return redirect("login")
        return HttpResponse("Error: Your data is saved but confirmation email failed to send.")
    

def confirm_email(request, token):
    try:
        email_confirm_object = ConfirmationToken.objects.get(token=token)
    except ConfirmationToken.DoesNotExist:
        return HttpResponse("Token invalid or expired!")
    user = email_confirm_object.user
    user.is_active = True
    user.is_confirmed_email = True
    user.save()
    email_confirm_object.delete()
    return redirect("login")

        


def login_view(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        email = request.POST.get("email", False)
        password = request.POST.get("password", False)
        if not email or not password:
            return HttpResponse("email and password required")
        user = authenticate(request, email = email, password = password)
        if user is not None:
            if user.is_confirmed_email:
                login(request, user)
                return redirect("home")
            else:   
                return HttpResponse("Ваш email еще не подтвержден. Пожалуйста, проверьте почту и подтвердите регистрацию.")
        return HttpResponse("Invalid credentials")
    

def home_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "home.html", {"user": request.user})



def logout_view(request):
    try:
        logout(request)
        return redirect("login")
    except Exception as ex:
        return HttpResponse("error " + str(ex))
        


def reset_password_view(request):
    if request.method == "POST":
        email = request.POST.get("email")

        if not CustomUser.objects.filter(email=email).exists():
            return HttpResponse("Отправленно ссылка на зарег email")

        user = CustomUser.objects.get(email=email)
        PasswordResetToken.objects.filter(user=user).delete()

        token_obj = PasswordResetToken.objects.create(user=user)
        reset_link = f"http://127.0.0.1:8002/auth/reset-password-confirm/{token_obj.token}/"

        send_mail(
            subject="Сброс пароля",
            message=f"Для сброса пароля перейдите по ссылке: {reset_link}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )

        return HttpResponse("Отправлена ссылка на email")
    return render(request, "reset_password.html")



def reset_password_confirm_view(request, token):
    token_obj = PasswordResetToken.objects.filter(token=token).first()
    if not token_obj:
        return HttpResponse("Ссылка недействительна или устарела.")

    if request.method == "POST":
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password!=confirm_password:
            return HttpResponse("Пароли не совпадают.")

        user = token_obj.user
        user.set_password(password)
        user.save()
        token_obj.delete()
        return redirect("login")

    return render(request, "reset_password_confirm.html")

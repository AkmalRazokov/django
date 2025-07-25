from django.urls import path
from .views import *
urlpatterns = [
    path('register/', register_view, name='register'),
    path('confirm-email/<uuid:token>/', confirm_email, name='confirm_email'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home_view, name='home'),

    path('reset-password/', reset_password_view, name='reset_password'),
    path('reset-password-confirm/<uuid:token>/', reset_password_confirm_view, name='reset_password_confirm'),
]
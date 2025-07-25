from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from .managers import CustomUserManager
import uuid

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_confirmed_email = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class ConfirmationToken(models.Model):
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    user = models.OneToOneField(CustomUser, related_name='confirmation', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class PasswordResetToken(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  
    token = models.UUIDField(default=uuid.uuid4, unique=True)      
    created_at = models.DateTimeField(auto_now_add=True)


class UserProfile(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    user = models.OneToOneField(CustomUser, related_name='profile', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
    
    class Meta:
        db_table='user_profile'
        managed=True
        verbose_name = 'user_profile'
        verbose_name_plural = 'user_profiles'

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from .managers import CustomUserManager
import uuid

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class Confirm_email(models.Model):
    token = models.UUIDField(uuid.uuid4)
    user = models.OneToOneField(CustomUser, related_name='user_id', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    


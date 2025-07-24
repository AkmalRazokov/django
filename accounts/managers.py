from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from .models import CustomUser



class CustomUserManager(BaseUserManager):
    def createuser(self, email, password, **extra_fields):
        if not email or not password:
            return ValueError("Please add email and password")
        email = self.normalize_email(email=email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def createsuperuser(self,email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True) 
        extra_fields.setdefault('is_confirmed_email', True) 
        
        return self.create_user(email=email, password=password, **extra_fields)







class UserProfile(models.Model):
    phone = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    user = models.OneToOneField(CustomUser, related_name='profile', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
    
    class Meta:
        db_table='user_profile'
        managed=True
        verbose_name = 'user_profile'
        verbose_name_plural = 'user_profiles'
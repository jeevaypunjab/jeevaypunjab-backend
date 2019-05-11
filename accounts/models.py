from django.contrib.auth.models import User
from django.db import models

from jeevaypunjab.regex_validators import phone_regex


class UserProfile(models.Model):
    """User profile with one to one relation with user"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(validators=[phone_regex], max_length=10,
                                    null=True, blank=True, unique=True)
    about = models.TextField(max_length=300, blank=True)
    profile_photo = models.ImageField(upload_to = 'profile_photos/',
                                      null=True, blank=True,)
    facebook = models.CharField(max_length=100, null=True,
                                blank=True, unique=True)
    instagram = models.CharField(max_length=100, null=True,
                                 blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'User Profile'

    def __str__(self):
        return str(self.user)

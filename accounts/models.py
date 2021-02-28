from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator, MaxValueValidator
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    
    # image = models.ImageField(null=True)
    first_name= models.CharField(max_length=50,null=True)
    last_name= models.CharField(max_length=50,null=True)
    # phone_regex = RegexValidator(regex=r'^[9|8|7|6]\d{9,15}', message="Phone number must be 10 digits allowed.")  
    # phone = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    # phone = models.IntegerField(null=True)
    # phone = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(9999999999)])
    phone = models.BigIntegerField(null=True)
    gender = models.BooleanField(default=False)
    age = models.IntegerField(null=True)
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
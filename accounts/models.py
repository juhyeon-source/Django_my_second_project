from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=10)
    birthday = models.DateField(
        validators=[
            MinValueValidator(date(1900, 1, 1)),
            MaxValueValidator(date.today())
        ]
    )
    
    REQUIRED_FIELDS = ['nickname', 'birthday']
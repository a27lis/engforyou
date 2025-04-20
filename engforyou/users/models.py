from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


class User(AbstractUser):
    age = models.PositiveSmallIntegerField(
        verbose_name='возраст',
        null=True,
        blank=True
    )
    
    
    
    


from django.db import models
from django.contrib.auth.models import AbstractUser

class RegisterUser(AbstractUser):
    email = models.EmailField(unique=True)
    last_period_date = models.DateField(blank= True, null=True)
    cycle_average = models.IntegerField(blank= True, null=True)
    period_average = models.IntegerField(blank= True, null=True)
    start_date = models.DateField(blank= True, null=True)
    end_date = models.DateField(blank= True, null=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = []
    


    def __str__(self):
        return f'{self.email}'


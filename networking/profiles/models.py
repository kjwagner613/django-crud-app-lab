from turtle import home
from django.db import models

# Create your models here.
class FieldOfWork(models.Model):
    name = models.CharField(max_length=100)
   
    
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    field_of_work = models.ForeignKey(FieldOfWork, on_delete=models.SET_NULL, null=True)
    DOB = models.DateField()
    spouse_name = models.CharField(max_length=100)
    spouse_DOB = models.DateField()
    home_state = models.CharField(max_length=100)
    home_city = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    linkedin_profile = models.URLField()
    
    
    def __str__(self):
        return self.user.username

from django.db import models
from datetime import date

class FieldOfWork(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    name = models.CharField(max_length=255, default='Enter Name')
    field_of_work = models.ForeignKey(FieldOfWork, on_delete=models.SET_NULL, null=True)
    DOB = models.DateField(default=date(2000, 1, 1))
    spouse_name = models.CharField(max_length=100, default='Not Specified')
    spouse_DOB = models.DateField(default=date(2000, 1, 1))
    home_state = models.CharField(max_length=100, default="Unknown State")
    home_city = models.CharField(max_length=100, default="Unknown City")
    phone_number = models.CharField(max_length=15, default="000-000-0000")
    email = models.EmailField(default='emailaddress@youremailserver.com')
    linkedin_profile = models.URLField(default='http://linkedin.com')

    def __str__(self):
        return self.name
    
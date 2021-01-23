from django.db import models

# Create your models here.
class Contacts(models.Model):
    name= models.CharField(max_length=100,default="")
    email= models.EmailField(max_length=254,default="",unique=True)
    phone_no= models.CharField(max_length=13,default="")
    
from django.contrib.auth.models import User
User._meta.get_field('email')._unique = True
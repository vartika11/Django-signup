from django.db import models

# Create your models here.
class Login(models.Model):
    name = models.CharField(max_length=200)
    #email =models.CharField(max_length=200)
    password = models.IntegerField()
    confirmpassword = models.IntegerField()






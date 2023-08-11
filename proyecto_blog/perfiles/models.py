from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    Last_Name = models.CharField(max_length=200)
    First_Name = models.CharField(max_length=200)
    Username = models.TextField()
    Email = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='users', blank=True, null=True)
    Password1 = models.DateTimeField(auto_now_add=True)
    Password2 = models.ImageField(upload_to='users', blank=True, null=True)

    def __str__(self):
        return self.Username
# Create your models here.



from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    gender_choice = [
        ('Male','Male'),
        ('female','female'),
        ('other','other')]

    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True, blank=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    phone = models.BigIntegerField()
    gender = models.CharField(max_length=200,choices=gender_choice)
    image = models.ImageField()
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name+' '+self.last_name


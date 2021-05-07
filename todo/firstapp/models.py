from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import get_user_model
import datetime

logged_user=get_user_model()
# Create your models here.

class user(User):
    def __str__(self):
        return self.first_name
class data(models.Model):
    user=models.ForeignKey(logged_user,on_delete=models.CASCADE,related_name='data')
    data=models.CharField(max_length=1000)
    date_created=models.DateField(default=timezone.now)
    list_length=models.IntegerField(default=0,unique=False)


    def __str__(self):
        return f"{self.user.username}-data"
    



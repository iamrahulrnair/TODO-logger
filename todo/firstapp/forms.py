from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms.models import ModelForm


class userregform(UserCreationForm):
    class Meta:
        model=models.user
        fields=['first_name','last_name','username']
        




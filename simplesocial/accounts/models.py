from django.db import models
from django.contrib import auth
# Create your models here.

class User(auth.models.User , auth.models.PermissionsMixin): # all work is done by django..

    def __str__(self):
        return '@{}'.format(self.username) # username comes with class User

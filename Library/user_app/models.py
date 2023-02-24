from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    class UserType(models.TextChoices):
        MEMBER = 'member'
        LIBRARIAN = 'librarian'

    usertype = models.CharField(max_length=50, choices=UserType.choices)


class MemberShip(models.Model):

    class Register(models.TextChoices):
        REGISTER = 'approved'
        CANCEL = 'cancel'
        NOTVERIFIED = 'notverified'

    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    aproval = models.CharField(max_length=50, choices=Register.choices)

    def __str__(self):
        return self.username

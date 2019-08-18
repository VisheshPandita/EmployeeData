from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
  age = models.IntegerField(default=18)
  phone = PhoneField(blank=False)
  department = models.CharField(max_length=50, default='')

  def __str__(self):
      return self.user.username
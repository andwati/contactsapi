from django.contrib.auth.models import User
from django.db import models


class Contact(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    country_code = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    contact_picture = models.URLField(null=True)
    is_favorited = models.BooleanField(default=True)

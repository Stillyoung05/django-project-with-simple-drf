from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    user_image = models.ImageField(default='media/default_user_image.jpg', upload_to='media/')
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.first_name
    
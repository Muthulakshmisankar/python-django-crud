from django.db import models

# Create your models here.
class employee(models.Model):
    fullname = models.TextField(max_length=100)
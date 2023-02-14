from django.db import models

# Create your models here.
class CRUD(models.Model):
    name = models.TextField()
    email = models.TextField(max_length=40)

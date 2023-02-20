from django.db import models

class MyMongoModel(models.Model):
    # Define fields for MongoDB model
    name = models.CharField(max_length=100)
    description = models.TextField()
    cid=models.CharField(max_length=100)
    # class Meta:
    #     db_table = 'collection_lakshmi'

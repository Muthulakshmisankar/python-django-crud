from rest_framework import viewsets
from .import models
from .import serializers
class CrudViewSets(viewsets.ModelViewSet):
    queryset =  models.CRUD.objects.all()
    serializer_class = serializers.CrudSerializer
    

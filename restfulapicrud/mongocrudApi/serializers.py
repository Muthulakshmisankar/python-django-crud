from rest_framework import serializers
from .models import MyMongoModel

class MyMongoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyMongoModel
        fields = ('name', 'description','cid')

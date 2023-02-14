from django.shortcuts import render
from rest_framework import generics
from .models import Note
from .serializers   import NoteSerializers
class NoteList(generics.ListCreateAPIView):
    queryset= Note.objects.all()
    serializer_class = NoteSerializers
    
class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializers
    



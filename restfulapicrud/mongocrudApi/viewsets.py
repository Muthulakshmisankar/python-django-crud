# from rest_framework import generics
# from .models import Note
# from .serializers import NoteSerializers

# class MyNoteList(generics.ListCreateAPIView):
#     queryset = Note.objects.using('mongoDb').all()
#     serializer_class = NoteSerializers

# class MyNoteDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Note.objects.using('mongoDb').all()
#     serializer_class = NoteSerializers
from rest_framework import generics
from .models import MyMongoModel
from .serializers import MyMongoSerializer


class MyMongoListCreateView(generics.ListCreateAPIView):
    serializer_class = MyMongoSerializer
    print('Serializer list')
    def get_queryset(self):
        queryset = MyMongoModel.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(cid=id)
        return queryset   


class MyMongoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyMongoModel.objects.all()
    serializer_class = MyMongoSerializer

class UpdateView(generics.UpdateAPIView):
    queryset = MyMongoModel.objects.all()
    serializer_class = MyMongoSerializer
    lookup_field = 'cid'
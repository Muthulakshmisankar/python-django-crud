from django.urls import path
from mongocrudApi import views

urlpatterns = [
    path('', views.MyMongoListCreateView.as_view()),
    path('<int:pk>/', views.MyMongoRetrieveUpdateDestroyView.as_view()),
        path('<int:pk>/', views.UpdateView.as_view() , name='mymongo-update')
]
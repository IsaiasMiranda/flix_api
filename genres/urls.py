from django.urls import path

from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('genres/', GenreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>', GenreRetrieveUpdateDestroyAPIView.as_view(), name='genre-detail-view'),
]

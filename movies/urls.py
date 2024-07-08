from django.urls import path

from movies.views import MovieListCreateAPIView, MovieRetrieveUpdateDestroyAPIView, MovieStatsView


urlpatterns = [
    path('movies/', MovieListCreateAPIView.as_view(), name='movie-create-list'),
    path('movies/<int:pk>', MovieRetrieveUpdateDestroyAPIView.as_view(), name='movie-detail-view'),
    path('movies/stats', MovieStatsView.as_view(), name='movie-stats-view')
]

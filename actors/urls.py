from django.urls import path

from actors.views import ActorListCreateAPIView, ActorRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('actors/', ActorListCreateAPIView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>', ActorRetrieveUpdateDestroyAPIView.as_view(), name='actor-detail-view'),
]

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from actors.models import Actor
from actors.serializers import ActorSerializer
from core.permissions import GlobalPermission


class ActorListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermission)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermission)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

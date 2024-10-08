from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from core.permissions import GlobalPermission
from reviews.models import Review
from reviews.serializers import ReviewSerializer


class ReviewListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermission)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermission)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

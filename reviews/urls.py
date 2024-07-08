from django.urls import path

from reviews.views import ReviewListCreateAPIView, ReviewRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('reviews/', ReviewListCreateAPIView.as_view(), name='review-create-list'),
    path('reviews/<int:pk>', ReviewRetrieveUpdateDestroyAPIView.as_view(), name='review-detail-view'),
]

from django.urls import path
from apps.reviews.views import (
    hotel_comments,
    review_delete,
    hotel_reviews,
    review_moderation,
    review_update,
    unmoderation,
)

urlpatterns = [
    path('<int:pk>/<int:parent>/', hotel_comments, name='review_create'),
    path('review-delete/<hotel>/<parent>/<int:pk>/', review_delete, name='review_delete'),
    path('hotel-reviews/<int:pk>/', hotel_reviews, name='hotel_reviews'),
    path('review-moderation/', review_moderation, name='review_moderation'),
    path('review-update/<int:pk>', review_update, name='review_update'),
    path('unmoderation/<int:pk>', unmoderation, name='unmoderation')
]
from django.urls import path
from . import views


urlpatterns = [
    path('reviews/', views.ReviewCreateListView.as_view(), name='review_create_list'),
    path('reviews/<int:pk>/', views.ReviewRetrieveUpdateDestoyView.as_view(), name='review-detail-view'),
]
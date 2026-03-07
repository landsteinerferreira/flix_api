from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyView
from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroyView
from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroyView
from reviews.views import ReviewCreateListView, ReviewRetrieveUpdateDestoyView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('genres/', GenreCreateListView.as_view(), name='genre_create_list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'),
    path('actors/', ActorCreateListView.as_view(), name='actor_create_list'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name='actor-datail-view'),
    path('movies/', MovieCreateListView.as_view(), name='movie_create_list'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='review-detail-view'),
    path('reviews/', ReviewCreateListView.as_view(), name='review_create_list'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestoyView.as_view(), name='review-detail-view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

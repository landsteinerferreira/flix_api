from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermition
from genres.models import Genre
from genres.serializers import GenreSerializer


# API com Django Rest Framework Create e List
class GenreCreateListView(generics.ListCreateAPIView):

    # Caso queira criar um filtro basta fazer
    # queryset = Genre.objects.filter(name='Terror')
    permission_classes = (IsAuthenticated, GlobalDefaultPermition)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


# API com Django Rest Framework Update e Delete
class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermition)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

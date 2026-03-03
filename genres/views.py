from rest_framework import generics
from genres.models import Genre
from genres.serializers import GenreSerializer


# API com Django Rest Framework Cria e Lista
class GenreCreateListView(generics.ListCreateAPIView):
    # Caso queira criar um filtro basta fazer
    #queryset = Genre.objects.filter(name='Terror')
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

# API com Django Rest Framework Cria e Lista
class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404 # Reporta erro 404
from genres.models import Genre
from rest_framework import generics

# LISTA E CRIA
@csrf_exempt
def genre_create_list_view(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        data = [{'id': genre.id, 'name': genre.name} for genre in genres]
        return JsonResponse(data, safe=False)
    
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8')) # Adequa o json com acentos
        new_genre = Genre(name=data['name']) # Cria um novo genero
        new_genre.save() # Salva no banco
        return JsonResponse(
            {'id': new_genre.id, 'name': new_genre.name},
            status=201,
        )

# DETALHE
@csrf_exempt
def genre_detail_view(request, pk):
    genre = get_object_or_404(Genre, pk=pk)

    if request.method == 'GET':
        data = {'id': genre.id, 'name': genre.name}
        return JsonResponse(data)
    

    # PUT - UPDATE
    elif request.method == 'PUT':
        # Carrega o objeto no padrão
        data = json.loads(request.body.decode('utf-8'))
        # Atualiza o objeto
        genre.name == data['name']
        # Salva
        genre.save()
        # Retorna o status
        return JsonResponse(
            {'id': genre.id, 'name': genre.name},

        )
    
    # DELETE
    elif request.method == 'DELETE':
        genre.delete()
        return JsonResponse(
            {'message': 'Gênero excluido com sucesso.'},
            status=204,
        )


    




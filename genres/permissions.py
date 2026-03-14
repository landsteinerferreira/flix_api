from rest_framework import permissions


class GenrePermitionClass(permissions.BasePermission):

    def has_permission(self, request, view):
        # Lógica da permissão
        print(f'Usuário: {request.user}')  # Usuario que solicitou a permissão
        print(f'View solicitada: {view}')  # View acessada

        # Exige que o usuario tenha visualização
        if request.method in ['GET', 'OPTIONS', 'HEAD']:
            return request.user.has_perm('genres.view_genre')
        # Exige que o usuario tenha adição
        if request.method == 'POST':
            return request.user.has_perm('genres.add_genre')

        if request.method in ['PATCH', 'PUT']:
            return request.user.has_perm('genres.change_genre')

        if request.method == ['DELETE']:
            return request.user.has_perm('genres.delete_genre')

        return False

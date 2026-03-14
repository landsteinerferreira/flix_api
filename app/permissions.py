from rest_framework import permissions


class GlobalDefaultPermition(permissions.BasePermission):

    # Função que descobre as permissões
    def has_permission(self, request, view):
        # Nome do app - Nome da Ação - Nome do modelo
        # f'{app_name}.{action_name}_{model_name}'

        model_permission_codename = self.__get_model_permission_codename(
            method=request.method,
            view=view,
        )
        if not model_permission_codename:
            return False

        return request.user.has_perm(model_permission_codename)

    # Função que pega os dados da solicitação
    def __get_model_permission_codename(self, method, view):
        try:
            model_name = view.queryset.model._meta.model_name  # Pega o nome do model
            app_label = view.queryset.model._meta.app_label  # Pega o nome do app
            action = self.__get_action_sufix(method)  # Pega a ação do usuário
            return f'{app_label}.{action}_{model_name}'  # Retorna os dados montados
        except AttributeError:
            return None

    # Função que detalha qual metodo será selecionado
    def __get_action_sufix(self, method):
        method_actions = {
            'GET': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete',
            'OPTIONS': 'view',
            'HEAD': 'view',
        }
        return method_actions.get(method, '')

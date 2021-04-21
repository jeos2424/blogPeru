#
from django.urls import path
from . import views

app_name = "favoritos_app"

urlpatterns = [
    path(
        'perfil/', 
        views.UserPageView.as_view(),
        name='fovorite_perfil',
    ),
    path(
        'favorito/<pk>/', 
        views.AddFavoriteView.as_view(),
        name='fovorite_add',
    ),
    path(
        'eliminar/<pk>/', 
        views.FavoriteDeleteView.as_view(),
        name='fovorite_delete',
    ),
]
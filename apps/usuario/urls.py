from django.urls import path, include
from apps.usuario.views import index, usuarioCreate, usuarioEli, usuarioEdit

app_name = "usuarios"
urlpatterns = [
    path('', index, name='index'),
    path('nuevo/', usuarioCreate, name='usuarioCreate'),
    path('actualizar/<int:id_usuario>/', usuarioEdit, name='usuarioEdit'),
    path('eliminar/<int:id_usuario>/', usuarioEli, name='usuarioEli'),
]
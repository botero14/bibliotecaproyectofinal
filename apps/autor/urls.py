from django.urls import path, include
from apps.autor.views import index, autorCreate, autorEli, autorEdit

app_name = "autores"
urlpatterns = [
    path('', index, name='index'),
    path('nuevo/', autorCreate, name='autorCreate'),
    path('actualizar/<int:id_autor>/', autorEdit, name='autorEdit'),
    path('eliminar/<int:id_autor>/', autorEli, name='autorEli'),
]
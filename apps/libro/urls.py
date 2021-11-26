from django.urls import path, include
from apps.libro.views import index, libroCreate, libroEli, libroEdit

app_name = "libros"
urlpatterns = [
    path('', index, name='index'),
    path('nuevo/', libroCreate, name='libroCreate'),
    path('actualizar/<int:id_libro>/', libroEdit, name='libroEdit'),
    path('eliminar/<int:id_libro>/', libroEli, name='libroEli'),
]
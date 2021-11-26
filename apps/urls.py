from django.urls import path, include
from apps.ejemplar.views import index, ejemplarCreate, ejemplarEli, ejemplarEdit

app_name = "ejemplares"
urlpatterns = [
    path('', index, name='index'),
    path('nuevo/', ejemplarCreate, name='ejemplarCreate'),
    path('actualizar/<int:id_ejemplar>/', ejemplarEdit, name='ejemplarEdit'),
    path('eliminar/<int:id_ejemplar>/', ejemplarEli, name='ejemplarEli'),
]
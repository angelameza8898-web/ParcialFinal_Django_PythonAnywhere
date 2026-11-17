from django.urls import path
from .views import crear_programa

urlpatterns = [
    path('programas/crear/', crear_programa, name='crear_programa'),
]

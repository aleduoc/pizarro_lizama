from django.urls import path
from .views import home, pagina02, pagina03, pagina04, pagina05, pagina06, pagina07

urlpatterns = [
    path('', home, name='home'),
    path('pagina02', pagina02, name='pagina02'),
    path('pagina03', pagina03, name='pagina03'),
    path('pagina04', pagina04, name='pagina04'),
    path('pagina05', pagina05, name='pagina05'),
    path('pagina06', pagina06, name='pagina06'),
    path('pagina07', pagina07, name='pagina07'),
]
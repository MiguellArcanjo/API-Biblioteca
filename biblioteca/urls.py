from rest_framework import routers
from biblioteca.views import BibliotecaViewSet, LivrariaViewSet

routers = routers.DefaultRouter()
routers.register(r'biblioteca', BibliotecaViewSet)
routers.register(r'livraria', LivrariaViewSet)
urlpatterns =  routers.urls
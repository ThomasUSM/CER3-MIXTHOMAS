from django.urls import path, include
from rest_framework import routers
from astro_gym_app import views
from .views import ClaseViewSet, home

router = routers.DefaultRouter()
router.register(r'clases', views.ClaseViewSet)

urlpatterns = [
    path('rest/',include(router.urls)),
    path('', home, name = 'astro_gym/base.html'),
]

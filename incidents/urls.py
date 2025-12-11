from django.urls import path, include
from rest_framework import routers
from .views import (
    FireIncidentViewSet, base_home, geoloc_view, prediction_view,
    alert_view, modelling_view, search_view, contact_view
)
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r'api/incidents', FireIncidentViewSet, basename='incidents')

urlpatterns = [
    # pages frontend (onglets)
    path('', base_home, name='home'),
    path('geolocalisation/', geoloc_view, name='geoloc'),
    path('prediction/', prediction_view, name='prediction'),
    path('alerte/', alert_view, name='alert'),
    path('modelisation/', modelling_view, name='modelling'),
    path('recherche/', search_view, name='search'),
    path('contact/', contact_view, name='contact'),
    path('testmap/', TemplateView.as_view(template_name='test_map.html'), name='testmap'),

    # API
    path('', include(router.urls)),
]

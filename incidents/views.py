from django.shortcuts import render
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework.views import APIView
from django.db.models import Count
from .models import FireIncident
from .serializers import FireIncidentSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions

# Frontend views (pages)
def base_home(request):
    # page d'accueil (dashboard simple)
    return render(request, 'home.html')

def geoloc_view(request):
    return render(request, 'geoloc.html')

def prediction_view(request):
    return render(request, 'prediction.html')

def alert_view(request):
    return render(request, 'alert.html')

def modelling_view(request):
    return render(request, 'modelling.html')

def search_view(request):
    return render(request, 'search.html')

def contact_view(request):
    return render(request, 'contact.html')

# API: pagination (utilisable)
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 200

# API ViewSet avec filtres/search/order + endpoint custom "recent" & "stats"
class FireIncidentViewSet(viewsets.ModelViewSet):
    queryset = FireIncident.objects.all().order_by('-date','-time')
    serializer_class = FireIncidentSerializer
    permission_classes = [permissions.AllowAny]  # changer en IsAuthenticated en prod
    pagination_class = StandardResultsSetPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'cause': ['exact'],
        'date': ['gte', 'lte', 'exact'],
    }
    search_fields = ['cause']
    ordering_fields = ['date','houses_burned','created_at']

    @action(detail=False, methods=['get'])
    def recent(self, request):
        qs = self.get_queryset()[:10]
        serializer = self.get_serializer(qs, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def stats(self, request):
        # statistiques simples : nombre par commune et par cause
        by_cause = FireIncident.objects.values('cause').annotate(total=Count('id')).order_by('-total')
        return Response({'by_cause': list(by_cause)})

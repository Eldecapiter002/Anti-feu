from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# drf spectacular
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Frontend de l'app incidents (pages)
    path('', include('incidents.urls')),

    # API schema /docs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

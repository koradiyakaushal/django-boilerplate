from os import name
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions

from .auth import CustomAuthToken, ping

from drf_yasg.views import get_schema_view # new
from drf_yasg import openapi # new

schema_view = get_schema_view(
    openapi.Info(
        title="Person API",
        default_version="v1",
        description="A sample API for learning DRF",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="hello@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)  


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui( # new
    'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui( # new
    'redoc', cache_timeout=0), name='schema-redoc'),

    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('', ping, name='ping'),
    # path('logs/', include('request_viewer.urls'))

    path('', include('app.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from config import settings
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny, ),
)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('lms.urls', namespace='lms')),
                  path('users/', include('users.urls', namespace='users')),

                  path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, re_path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from work.views import allWorks

# jazzmin settings
routers = routers.DefaultRouter()

schema_view = get_schema_view(
    openapi.Info(
        title="Rookmate",
        default_version='v1',
        description="Rookmate API 문서",
        terms_of_service="https://www.google.com/policies/terms/",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# project settings
urlpatterns = [
    path('admin/', admin.site.urls),
    # root
    path('', allWorks),
    # user
    path('users/', include('user.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# swagger settings
urlpatterns += [
    re_path(r'^(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


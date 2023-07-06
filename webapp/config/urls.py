from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework import routers

from bookmark.views import RootBookmarkListAPIView, RootBookmarkRetrieveDestroyAPIView, WorkBookmarkListCreateAPIView, WorkBookmarkRetrieveDestroyAPIView
from work.views import RootWorkRetrieveAPIView, RootWorkListAPIView, WorkLikeListCreateAPIView

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
    # root work
    path('works/', RootWorkListAPIView.as_view()),
    path('works/<uuid:work_uuid>/', RootWorkRetrieveAPIView.as_view()),
    # root work - like
    path("works/<uuid:work_uuid>/likes/", WorkLikeListCreateAPIView.as_view()),
    # root work - work bookmark
    path('works/<uuid:work_uuid>/bookmarks/', WorkBookmarkListCreateAPIView.as_view()),
    path('works/<uuid:work_uuid>/bookmarks/<uuid:work_bookmark_uuid>/', WorkBookmarkRetrieveDestroyAPIView.as_view()),
    # root bookmark - root bookmark
    path('bookmarks/', RootBookmarkListAPIView.as_view()),
    path('bookmarks/<uuid:root_bookmark_uuid>/', RootBookmarkRetrieveDestroyAPIView.as_view()),
    # user
    path('users/', include('user.urls')),
    # portfolio
    path('portfolios/', include('portfolio.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# swagger settings
urlpatterns += [
    re_path(r'^(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


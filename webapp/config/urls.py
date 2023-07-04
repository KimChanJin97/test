from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework import routers

from bookmark.views import RootBookmarkListAPIView, RootBookmarkRetrieveDestroyAPIView, WorkBookmarkCreateAPIView, WorkBookmarkRetrieveDestroyAPIView
from work.views import RootWorkRetrieveAPIView, RootWorkListAPIView

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
    path('works/<int:work_id>', RootWorkRetrieveAPIView.as_view()),
    # root work - work bookmark
    path('works/<int:work_id>/bookmarks/', WorkBookmarkCreateAPIView.as_view()),
    path('works/<int:work_id>/bookmarks/<int:work_bookmark_id>', WorkBookmarkRetrieveDestroyAPIView.as_view()),
    # root bookmark - root bookmark
    path('bookmarks/', RootBookmarkListAPIView.as_view()),
    path('bookmarks/<int:root_bookmark_id>', RootBookmarkRetrieveDestroyAPIView.as_view()),
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


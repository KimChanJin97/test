from django.urls import path
from bookmark.views import WorkBookmarkCreateAPIView, WorkBookmarkRetrieveDestroyAPIView

app_name = 'bookmark'

urlpatterns = [
    path('', WorkBookmarkCreateAPIView.as_view()),
    path('<uuid:work_bookmark_uuid>/', WorkBookmarkRetrieveDestroyAPIView.as_view()),
]

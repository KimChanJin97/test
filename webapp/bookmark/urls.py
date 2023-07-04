from django.urls import path
from bookmark.views import WorkBookmarkCreateAPIView, WorkBookmarkRetrieveDestroyAPIView

app_name = 'bookmark'

urlpatterns = [
    path('', WorkBookmarkCreateAPIView.as_view()),
    path('<int:work_bookmark_id>/', WorkBookmarkRetrieveDestroyAPIView.as_view()),
]

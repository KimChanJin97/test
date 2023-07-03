from django.urls import path
from bookmark.views import BookmarkCreateAPIView, BookmarkRetrieveUpdateDestroyAPIView

app_name = 'bookmark'

urlpatterns = [
    path('', BookmarkCreateAPIView.as_view()),
    path('<int:bookmark_id>/', BookmarkRetrieveUpdateDestroyAPIView.as_view()),
]

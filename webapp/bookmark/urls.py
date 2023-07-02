from django.urls import path
from bookmark.views import BookmarkListCreateAPIView, BookmarkRetrieveUpdateDestroyAPIView

app_name = 'bookmark'

urlpatterns = [
    path('', BookmarkListCreateAPIView.as_view()),
    path('<int:bookmark_id>/', BookmarkRetrieveUpdateDestroyAPIView.as_view())
]

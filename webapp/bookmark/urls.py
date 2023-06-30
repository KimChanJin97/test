from django.urls import path
from bookmark.views import BookmarkListCreateAPIView, BookmarkRetrieveDestroyAPIView

urlpatterns = [
    path('', BookmarkListCreateAPIView.as_view()),
    path('<int:bookmark_id>/', BookmarkRetrieveDestroyAPIView.as_view())
]

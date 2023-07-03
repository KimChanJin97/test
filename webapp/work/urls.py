from django.urls import path, include
from work.views import WorkListCreateAPIView, WorkRetrieveUpdateDestroyAPIView
from bookmark.views import RootBookmarkCreateAPIView, RootBookmarkRetrieveDestroyAPIView

app_name = 'work'

urlpatterns = [
    path("", WorkListCreateAPIView.as_view()),
    path("<int:work_id>/", WorkRetrieveUpdateDestroyAPIView.as_view()),
    # bookmarkCreateAPIView, bookmarkRetrieveDestroy
    path("<int:work_id>/bookmarks/", RootBookmarkCreateAPIView.as_view()),
    path("<int:work_id>/bookmarks/<int:bookmark_id>", RootBookmarkRetrieveDestroyAPIView.as_view()),
    # path("<int:work_id>/bookmarks/<int:bookmark_id>", incldue())
]

from django.urls import path, include
from work.views import WorkListCreateAPIView, WorkRetrieveUpdateDestroyAPIView, WorkCommentListCreateAPIView, WorkCommentRetrieveUpdateDestroyAPIView
from bookmark.views import WorkBookmarkCreateAPIView, WorkBookmarkRetrieveDestroyAPIView


app_name = 'work'

urlpatterns = [
    path("", WorkListCreateAPIView.as_view()),
    path("<uuid:work_uuid>/", WorkRetrieveUpdateDestroyAPIView.as_view()),
    # work - bookmark
    path("<uuid:work_uuid>/work_bookmarks/", WorkBookmarkCreateAPIView.as_view()),
    path("<uuid:work_uuid>/work_bookmarks/<uuid:bookmark_uuid>/", WorkBookmarkRetrieveDestroyAPIView.as_view()),
    # work - workComment
    path("<uuid:work_uuid>/work_comments/", WorkCommentListCreateAPIView.as_view()),
    path("<uuid:work_uuid>/work_comments/<uuid:work_comment_uuid>/", WorkCommentRetrieveUpdateDestroyAPIView.as_view()),
]

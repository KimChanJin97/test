from django.urls import path, include
from work.views import WorkListCreateAPIView, WorkRetrieveUpdateDestroyAPIView, WorkCommentListCreateAPIView, WorkCommentRetrieveUpdateDestroyAPIView
from bookmark.views import WorkBookmarkCreateAPIView, WorkBookmarkRetrieveDestroyAPIView


app_name = 'work'

urlpatterns = [
    path("", WorkListCreateAPIView.as_view()),
    path("<int:work_id>/", WorkRetrieveUpdateDestroyAPIView.as_view()),
    # work - bookmark
    path("<int:work_id>/work_bookmarks/", WorkBookmarkCreateAPIView.as_view()),
    path("<int:work_id>/work_bookmarks/<int:bookmark_id>", WorkBookmarkRetrieveDestroyAPIView.as_view()),
    # work - workComment
    path("<int:work_id>/work_comments/", WorkCommentListCreateAPIView.as_view()),
    path("<int:work_id>/work_comments/<int:work_comment_id>", WorkCommentRetrieveUpdateDestroyAPIView.as_view()),
]

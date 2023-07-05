from django.urls import path

from outsourcing.views.outsourcing import OutsourcingListCreateAPIView, OutsourcingRetrieveUpdateAPIView
from outsourcing.views.outsourcing_comment import OutsourcingCommentRetrieveUpdateDestroyAPIView, OutsourcingCommentListCreateAPIView

app_name = 'outsourcing'

urlpatterns = [
    # outsourcing
    path("", OutsourcingListCreateAPIView.as_view()),
    path("<int:os_uuid>/", OutsourcingRetrieveUpdateAPIView.as_view()),
    # outsourcing - outsourcingComment
    path("<int:os_uuid>/outsourcing_comments/", OutsourcingCommentListCreateAPIView.as_view()),
    path("<int:os_uuid>/outsourcing_comments/<int:osc_uuid>/",OutsourcingCommentRetrieveUpdateDestroyAPIView.as_view()),
]

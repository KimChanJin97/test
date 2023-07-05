from django.urls import path

from outsourcing.views.outsourcing import OutsourcingListCreateAPIView, OutsourcingRetrieveUpdateAPIView
from outsourcing.views.outsourcing_comment import OutsourcingCommentRetrieveUpdateDestroyAPIView, OutsourcingCommentListCreateAPIView

app_name = 'outsourcing'

urlpatterns = [
    # outsourcing
    path("", OutsourcingListCreateAPIView.as_view()),
    path("<uuid:os_uuid>/", OutsourcingRetrieveUpdateAPIView.as_view()),
    # outsourcing - outsourcingComment
    path("<uuid:os_uuid>/outsourcing_comments/", OutsourcingCommentListCreateAPIView.as_view()),
    path("<uuid:os_uuid>/outsourcing_comments/<uuid:osc_uuid>/",OutsourcingCommentRetrieveUpdateDestroyAPIView.as_view()),
]

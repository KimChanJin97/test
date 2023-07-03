from django.urls import path

from outsourcing.views import OutsourcingListCreateAPIView, OutsourcingRetrieveUpdateAPIView, \
    OutsourcingCommentRetrieveUpdateDestroyAPIView, OutsourcingCommentListCreateAPIView, \
    OutsourcingContractListCreateAPIView, OutsourcingContractRetrieveUpdateAPIView

app_name = 'outsourcing'

urlpatterns = [
    # outsourcing
    path("", OutsourcingListCreateAPIView.as_view()),
    path("<int:outsourcing_id>/", OutsourcingRetrieveUpdateAPIView.as_view()),
    # outsourcing - outsourcingComment
    path("<int:outsourcing_id>/comments/", OutsourcingCommentListCreateAPIView.as_view()),
    path("<int:outsourcing_id>/comments/<int:outsourcing_comment_id>", OutsourcingCommentRetrieveUpdateDestroyAPIView.as_view()),
    # outsourcing - outsourcingContract
    path("<int:outsourcing_id>/contracts/", OutsourcingContractListCreateAPIView.as_view()),
    path("<int:outsourcing_id>/contracts/<int:outsourcing_contract_id>", OutsourcingContractRetrieveUpdateAPIView.as_view()),
]

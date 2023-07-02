from django.urls import path
from outsourcing.views import OutsourcingListCreateAPIView, OutsourcingRetrieveUpdateAPIView

app_name = 'outsourcing'

urlpatterns = [
    path("", OutsourcingListCreateAPIView.as_view()),
    path("<int:outsourcing_id>/", OutsourcingRetrieveUpdateAPIView.as_view()),
]
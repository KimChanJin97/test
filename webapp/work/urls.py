from django.urls import path
from work.views import WorkListCreateAPIView, WorkRetrieveUpdateDestroyAPIView

app_name = 'work'

urlpatterns = [
    path("", WorkListCreateAPIView.as_view()),
    path("<int:work_id>/", WorkRetrieveUpdateDestroyAPIView.as_view()),
]

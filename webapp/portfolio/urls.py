from django.urls import path, include
from portfolio.views import PortfolioRetrieveUpdateAPIView, PortfolioListAPIView

app_name = 'portfolio'

urlpatterns = [
    path('', PortfolioListAPIView.as_view()),
    path('<int:portfolio_id>/', PortfolioRetrieveUpdateAPIView.as_view()),
    path('<int:portfolio_id>/works/', include('work.urls')),
]

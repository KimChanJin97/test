from django.urls import path, include
from portfolio.views import PortfolioRetrieveUpdateAPIView, PortfolioListCreateAPIView

app_name = 'portfolio'

urlpatterns = [
    # portfolio
    path('', PortfolioListCreateAPIView.as_view()),
    path('<int:portfolio_id>/', PortfolioRetrieveUpdateAPIView.as_view()),
    # portfolio - work
    path('<int:portfolio_id>/works/', include('work.urls')),
    # portfolio - outsourcing
    path('<int:portfolio_id>/outsourcings/', include('outsourcing.urls')),
]

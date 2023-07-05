from django.urls import path, include
from portfolio.views import PortfolioRetrieveUpdateAPIView, PortfolioListCreateAPIView, PortfolioAbilityListCreateAPIView, PortfolioAbilityRetrieveUpdateDestroyAPIView, PortfolioCommentListCreateAPIView, PortfolioCommentRetrieveUpdateDestroyAPIView

app_name = 'portfolio'

urlpatterns = [
    # portfolio
    path('', PortfolioListCreateAPIView.as_view()),
    path('<uuid:portfolio_uuid>/', PortfolioRetrieveUpdateAPIView.as_view()),
    # portfolio - portfolio ability
    path('<uuid:portfolio_uuid>/portfolio_abilities/', PortfolioAbilityListCreateAPIView.as_view()),
    path('<uuid:portfolio_uuid>/portfolio_abilities/<uuid:portfolio_ability_uuid>', PortfolioAbilityRetrieveUpdateDestroyAPIView.as_view()),
    # portfolio - portfolio comment
    path('<uuid:portfolio_uuid>/portfolio_comments/', PortfolioCommentListCreateAPIView.as_view()),
    path('<uuid:portfolio_uuid>/portfolio_comments/<uuid:portfolio_comment_uuid>', PortfolioCommentRetrieveUpdateDestroyAPIView.as_view()),
    # portfolio - work
    path('<uuid:portfolio_uuid>/works/', include('work.urls')),
    # portfolio - outsourcing
    path('<uuid:portfolio_uuid>/outsourcings/', include('outsourcing.urls')),
]

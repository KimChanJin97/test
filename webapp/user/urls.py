from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from user.views import kakaoCallback, kakaoGetLogin, UserRetrieveUpdateAPIView, UserListAPIView, DjangoRegisterAPIView, DjangoLoginAPIView

urlpatterns = [
    # kakao login
    path('kakao/login/', kakaoGetLogin),
    path('kakao/callback/', kakaoCallback),
    # drf signup, singin
    path('registration/', DjangoRegisterAPIView.as_view()),
    path('login/', DjangoLoginAPIView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view()),
    # user
    path('', UserListAPIView.as_view()),
    path('<int:user_id>/', UserRetrieveUpdateAPIView.as_view()),
    # user - bookmark
    path('<int:user_id>/bookmarks/', include('bookmark.urls')),
    # user - portfolio
    path('<int:user_id>/portfolios/', include('portfolio.urls')),
]

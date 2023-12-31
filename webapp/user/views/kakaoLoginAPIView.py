import requests
from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from config.settings.base import SOCIAL_OUTH_CONFIG
from user.models import User


@api_view(['GET'])
@permission_classes([AllowAny, ])
def kakaoGetLogin(request):
    """
    [ 설명 ]
    - 프론트에서 카카오 로그인 버튼을 클릭
    - 카카오 로그인 화면으로 리다이렉트
    - 카카오 로그인
    - 클라이언트 정보 제공 동의
    - localhost:8000/user/kakao/callback 로 인가코드 전달
    - kakaoCallback() 함수 실행
    """
    CLIENT_ID = SOCIAL_OUTH_CONFIG['KAKAO_REST_API_KEY']
    REDIRET_URL = SOCIAL_OUTH_CONFIG['KAKAO_REDIRECT_URI']
    url = f"https://kauth.kakao.com/oauth/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRET_URL}&response_type=code"
    return redirect(url)


@api_view(['GET'])
@permission_classes([AllowAny, ])
def kakaoCallback(request):
    """
    [ 설명 ]
    - 전달받은 인가코드 파싱
    - 인가코드를 사용하여 ACCESS TOKEN, REFRESH TOKEN 을 카카오 인증 서버에 post 요청
    - 카카오 인증 서버가 사용자 정보를 보내줌
    """
    url = "https://kauth.kakao.com/oauth/token"
    code = request.GET.get("code")
    isMember = True
    if code is None:
        raise Exception("code is none")

    res = {
        'grant_type': 'authorization_code',
        "client_id": SOCIAL_OUTH_CONFIG['KAKAO_REST_API_KEY'],
        "redirect_uri": SOCIAL_OUTH_CONFIG['KAKAO_REDIRECT_URI'],
        'code': code,
    }
    token_response = requests.post(url, data=res)
    access_token = token_response.json().get('access_token')
    user_info_response = requests.get('https://kapi.kakao.com/v2/user/me',headers={"Authorization": f'Bearer {access_token}'})
    profile_json = user_info_response.json()
    kakao_account = profile_json.get("kakao_account")
    kakaoId = profile_json.get("id")
    kakao_thumbnail_url = profile_json.get("properties").get("thumbnail_image")
    email = kakao_account.get("email", None)

    if email is None:
        return JsonResponse({'err_msg': 'failed to get email'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(kakaoId=kakaoId).exists():
        user_info = User.objects.get(kakaoId=kakaoId)
        refresh = RefreshToken.for_user(user_info)
        isMember = True
        data = {
            'user': str(user_info),
            'token': str(refresh.access_token),
            'email': email,
            'exist': True,
            'isMember': isMember
        }
        return Response(data)
        # return HttpResponse(
        #     f'user:{user_info}, token:{str(refresh.access_token)}, email:{email}, exist:true, isMember:{isMember}')

    else:
        User(
            kakaoId=kakaoId,
            kakao_thumbnail_url=kakao_thumbnail_url,
            email=email,
        ).save()
        user_info = User.objects.get(kakaoId=kakaoId)
        # serializer = UserSerializer(data=user_info)
        # if not serializer.is_valid():
        #     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        refresh = RefreshToken.for_user(user_info)
        isMember = False
        data = {
            'user': str(user_info),
            'token': str(refresh.access_token),
            'email': email,
            'exist': True,
            'isMember': isMember
        }
        return Response(data)
        # return HttpResponse(
        #     f'user:{user_info}, token:{str(refresh.access_token)}, email:{email}, exist:true, isMember:{isMember}')

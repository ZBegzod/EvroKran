from rest_framework import status
from django.urls import reverse
from rest_framework.response import Response
from rest_framework import generics, views
from django.contrib.auth import login
from rest_framework.permissions import AllowAny
from apps.accounts.models import CustomUser
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .Utils import Util
from django.utils.encoding import (
    smart_str,
    smart_bytes,
    DjangoUnicodeDecodeError
)
from django.utils.http import (
    urlsafe_base64_decode,
    urlsafe_base64_encode
)
from django.contrib.sites.shortcuts import get_current_site
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import (
    LoginSerializer,
    RegisterModelSerializer,
    SetNewPasswordSerializer,
    ResetPasswordEmailRequestSerializer
)


class RegisterAPIView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterModelSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        print(user_data.get('phone_number'), 'user phone')
        user = CustomUser.objects.get(phone_number=user_data.get('phone_number'))
        token = RefreshToken.for_user(user)
        if user:
            return Response(data=str(token.access_token), status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)


class LoginAPIView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        refresh = RefreshToken.for_user(user)

        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

        return Response(data=data, status=status.HTTP_202_ACCEPTED)


class ResetPasswordRequestEmailAPIView(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer

    def post(self, request):
        phone_number = self.request.user.phone_number
        if CustomUser.objects.filter(phone_number=phone_number).exists():
            user = CustomUser.objects.get(phone_number=phone_number)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(request=request).domain
            relative_link = reverse('password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})
            abs_url = 'http://' + current_site + relative_link
            email_body = 'Hello \n Use link below to reset your password \n' + abs_url

            data = {
                'email_body': email_body,
                'to_email': user.email,
                'email_subject': 'Reset your password'
            }
            Util.send_email(data=data)
        return Response({'We have sent you link to reset your password'}, status=status.HTTP_200_OK)


class PasswordTokenCheckAPI(views.APIView):

    def get(self, request, uidb64, token):

        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response(
                    {'error': 'Token is not valid, please request a new one'},
                    status=status.HTTP_401_UNAUTHORIZED
                )

            return Response(
                {'success': True, 'message': 'Credentials valid', 'uidb64': uidb64, 'token': token},
                status=status.HTTP_200_OK
            )

        except DjangoUnicodeDecodeError as identifier:
            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error': 'Token is not valid, please request a new  one'},
                                status=status.HTTP_401_UNAUTHORIZED)


class SetPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)

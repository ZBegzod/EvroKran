from rest_framework import serializers, status
from apps.accounts.models import CustomUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from rest_framework.exceptions import AuthenticationFailed


class RegisterModelSerializer(serializers.ModelSerializer):
    confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ['phone_number', 'email',
                  'first_name', 'last_name',
                  'password', 'confirm',
                  ]

    #
    # def validate_password(self, attrs):
    #     password = attrs.get('password')
    #     confirm = attrs.get('confirm')
    #     if password != confirm:
    #         raise serializers.ValidationError({'detail': False, 'message': 'password did not match!'})
    #
    #     return password

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        phone_number_exists = CustomUser.objects.filter(phone_number=phone_number).first()
        if phone_number_exists:
            raise serializers.ValidationError({'detail': False, 'message': 'Phone number exists'})

        return attrs

    def create(self, validated_data):
        phone_number = validated_data['phone_number']
        email = self.data.get('email')
        password = self.data.get('password')
        first_name = self.data.get('first_name')
        last_name = self.data.get('last_name')
        hashed_password = make_password(password)
        print(phone_number, 'serializer phone')
        user = CustomUser.objects.create(

            phone_number=phone_number,
            password=hashed_password,
            email=email,
            first_name=first_name,
            last_name=last_name,

        )

        user.save()

        return user


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)
    confirm = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')
        confirm = attrs.get('confirm')

        if password == confirm:
            user_exists = CustomUser.objects.filter(phone_number=phone_number).first()
            if user_exists is not None:
                msg = 'User not Found!'
                serializers.ValidationError(msg, code=status.HTTP_403_FORBIDDEN)
        else:
            msg = 'Both "phone number" and "password" are required.'
            raise serializers.ValidationError(msg, code=status.HTTP_400_BAD_REQUEST)

        attrs['user'] = user_exists
        return attrs


class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=150, required=True, write_only=True)

    class Meta:
        fields = ['email']


class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        min_length=6, max_length=70, write_only=True
    )
    confirm = serializers.CharField(
        min_length=6, max_length=70, write_only=True
    )
    token = serializers.CharField(
        min_length=1, write_only=True
    )
    uidb64 = serializers.CharField(
        min_length=1, write_only=True
    )

    class Meta:
        fields = ['password', 'confirm', 'token', 'uidb64']

    def validate(self, attrs):

        try:
            password = attrs.get('password')
            confirm = attrs.get('confirm')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = force_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The reset link invalid', 401)

            if password != confirm:
                raise serializers.ValidationError('confirm password does not match')

            user.set_password(password)
            user.save()

        except Exception as e:
            raise AuthenticationFailed('The reset link invalid', 401)

        return super().validate(attrs)

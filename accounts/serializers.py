from rest_framework import serializers
from django.core.validators import validate_email
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User, OTP
from .utils import send_otp
import random


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['phone'] = user.phone
        token['username'] = user.username
        token['is_active'] = user.is_active
        token['is_admin'] = user.is_admin
        token['is_superuser'] = user.is_superuser

        return token
    
class UserLogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

class UserRegisterSerializer(serializers.Serializer):
    phone = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField(required = False , validators=[validate_email])
    password = serializers.CharField()
    confirm_password = serializers.CharField()
    
    def validate_phone(self, value):
        user = User.objects.filter(phone = value)
        if user.exists():
            raise serializers.ValidationError("Phone number already exists.")
        return value
    
    def validate_email(self, value):
        if User.objects.filter(email = value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value
    
    def validate(self, attrs):
        if attrs["password"] and attrs["confirm_password"] and attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError("The passwords do not match.")
        return attrs
    
    def create(self, validated_data):
        phone = validated_data["phone"]
        username = validated_data["username"]
        password = validated_data["password"]
        email = validated_data.get("email")
        random_code = random.randint(100000,999999)

        send_otp(phone, random_code)
        obj, created = OTP.objects.update_or_create(phone = phone, defaults={"code":random_code})
        return {"phone":phone, "code":random_code, "username":username, "email":email, "password":password}
    
class UserRegisterVerifySerializer(serializers.Serializer):
    code = serializers.IntegerField()

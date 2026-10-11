from django.core.validators import validate_email
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User
from .utils import send_otp
from .otp_service import ServiceOtp


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['phone'] = user.phone
        token['username'] = user.username
        token['is_active'] = user.is_active
        token['is_staff'] = user.is_staff
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
        ServiceOtp.generate_otp(phone)
        return {"phone":phone, "username":username, "email":email, "password":password}
    
class UserRegisterVerifySerializer(serializers.Serializer):
    code = serializers.IntegerField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("__all__")
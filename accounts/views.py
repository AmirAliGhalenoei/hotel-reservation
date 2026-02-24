from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import (
    MyTokenObtainPairSerializer,
    UserLogoutSerializer,
    UserRegisterSerializer,
    UserRegisterVerifySerializer,
    )
from .models import User, OTP
from .utils import send_otp
import random


class UserLoginAPIView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class UserLogoutAPIView(APIView):
    serializer_class = UserLogoutSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer_data = self.serializer_class(data = request.data)
        if serializer_data.is_valid():
            refresh_token = serializer_data.validated_data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message":"Deleted refresh_token successfuly"}, status=status.HTTP_200_OK)
        return Response(data=serializer_data.errors,status=status.HTTP_400_BAD_REQUEST)

class UserRegisterAPIView(APIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer_data = self.serializer_class(data = request.data)
        if serializer_data.is_valid():
            user_data = serializer_data.save()
            request.session["user_register"] = {
                "phone":user_data["phone"],
                "username":user_data["username"],
                "email":user_data["email"],
                "password":user_data["password"],
            }
            return Response({"message":f"Send code to {user_data["phone"]}"}, status=status.HTTP_201_CREATED)
        return Response(data=serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserRegiterVerifyCodeAPIView(APIView):
    serializer_class = UserRegisterVerifySerializer

    def post(self, request):
        session_user = request.session["user_register"]
        print("======",session_user)
        otp = OTP.objects.get(phone = session_user.get("phone"))
        serializer_data = self.serializer_class(data = request.data)
        if serializer_data.is_valid():
            code = serializer_data.validated_data.get("code")
            if code == otp.code:
                User.objects.create(
                    phone = session_user["phone"],
                    username = session_user["username"],
                    email = session_user.get("email",""),
                    password = session_user["password"],
                )
                otp.delete()
                return Response({"message":"The validation code was correct."}, status=status.HTTP_200_OK)
            return Response({"message":"The validation code was incorrect!!!."}, status=status.HTTP_200_OK)
        return Response(data = serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)
            



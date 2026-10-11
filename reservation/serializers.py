from rest_framework import serializers
from .models import Bespeak
from hotels.serializers import RoomSerializer
from accounts.serializers import UserSerializer


class BespeakSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    room = RoomSerializer(read_only=True)
    
    class Meta:
        model = Bespeak
        fields = ("__all__")

    def get_user(self, obj):
        return {
            "phone": obj.user.phone,
            "username": obj.user.username,
        }

class CreateBespeakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bespeak
        exclude = ("user", "room", "asking_price", "reserved")

 
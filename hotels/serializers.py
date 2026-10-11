from rest_framework import serializers
from .models import (
    Room,
    Hotel, 
    Cities, 
    RoomGalery,
    HotelGalery,
    RoomFacility, 
    HotelFacility,   
)


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = ("name",'slug')

    def create(self, validated_data):
        city = Cities.objects.create(**validated_data)
        return city
       
class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelFacility
        fields = ("title",)

    def create(self, validated_data):
        facility = HotelFacility.objects.create(**validated_data)
        return facility

class HotelGalerySerializer(serializers.ModelSerializer):
    hotel = serializers.PrimaryKeyRelatedField(queryset=Hotel.objects.filter(active=True))

    class Meta:
        model = HotelGalery
        fields = ("image", "hotel")

class RoomGalerySerializer(serializers.ModelSerializer):
    hotel = serializers.PrimaryKeyRelatedField(queryset=Hotel.objects.filter(active=True))
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.filter(available=True))

    class Meta:
        model = RoomGalery
        fields = ("image", "hotel", "room")

class RoomSerializer(serializers.ModelSerializer):
    facilitys = serializers.StringRelatedField(read_only=True,many=True)
    hotel = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Room
        fields = ("__all__")

class HotelSerializer(serializers.ModelSerializer):
    facilitys = serializers.StringRelatedField(read_only=True,many=True)
    city = serializers.StringRelatedField(read_only=True)
    hotel_galerys = serializers.SerializerMethodField()
    room_galerys = serializers.SerializerMethodField()
    rooms = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = ("__all__")
    
    def get_hotel_galerys(self, obj):
        result = obj.galerys.all()
        return HotelGalerySerializer(instance=result,many=True).data
    
    def get_room_galerys(self, obj):
        result = obj.room_galerys.all()
        return RoomGalerySerializer(instance=result,many=True).data
    
    def get_rooms(self, obj):
        result = obj.rooms.filter(available=True)
        return RoomSerializer(instance=result,many=True).data

    def create(self, validated_data):
        hotel = Hotel.objects.create(**validated_data)
        return  hotel

class CreateUpdateHotelSerializer(serializers.ModelSerializer):
    facilitys = serializers.PrimaryKeyRelatedField(queryset=HotelFacility.objects.all(), many=True)
    city = serializers.PrimaryKeyRelatedField(queryset=Cities.objects.all())

    class Meta:
        model = Hotel
        fields = ["name", "slug", "description", "address", "facilitys", "city", "star", "image"]

    # def create(self, validated_data):
    #     facilitys_data = validated_data.pop("facilitys",[])
    #     hotel = Hotel.objects.create(**validated_data)
    #     hotel.facilitys.set(facilitys_data)
    #     return hotel


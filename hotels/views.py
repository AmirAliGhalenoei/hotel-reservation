from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser
from .serializers import (
    CitiesSerializer,
    FacilitySerializer,
    HotelGalerySerializer,
    RoomGalerySerializer,
    HotelSerializer,
    CreateUpdateHotelSerializer
)
from .models import (
    Room,
    Hotel, 
    Cities, 
    RoomGalery,
    HotelGalery,
    RoomFacility, 
    HotelFacility,   
)


class CityViewSet(viewsets.ViewSet):
    permission_classes = [IsAdminUser,]
    serializer_class = CitiesSerializer
    queryset = Cities.objects.all()

    def list(self, request):
        serializer_data = self.serializer_class(instance=self.queryset.all(), many=True)
        return Response(
            data = serializer_data.data,
            status= status.HTTP_200_OK
        )
    
    def retrieve(self, request, pk=None):
        queryset = get_object_or_404(self.queryset, slug = pk)
        serializer_data = self.serializer_class(instance = queryset)
        return Response(
            data = serializer_data.data,
            status= status.HTTP_200_OK
        )
    
    def partial_update(self, request, pk=None):
        queryset = get_object_or_404(self.queryset, slug=pk)
        serializer_data = self.serializer_class(instance=queryset, data=request.data, partial=True)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(
                data = serializer_data.data,
                status= status.HTTP_200_OK
            )
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        queryset = get_object_or_404(self.queryset, slug = pk)
        queryset.delete()
        return Response({"message":"Deleted successfuly"}, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer_data = self.serializer_class(data = request.data)
        if serializer_data.is_valid():
            serializer_data.create(serializer_data.validated_data)
            return Response(
                data = serializer_data.data,
                status= status.HTTP_201_CREATED
            )
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)

class FacilityViewSet(viewsets.ViewSet):
    permission_classes = [IsAdminUser,]
    serializer_class = FacilitySerializer
    queryset = HotelFacility.objects.all()

    def list(self, request):
        serializer_data = self.serializer_class(instance=self.queryset, many=True)
        return Response(
            data=serializer_data.data,
            status=status.HTTP_200_OK
        )
    
    def retrieve(self, request, pk):
        queryset = get_object_or_404(self.queryset, pk=pk)
        serializer_data = self.serializer_class(instance = queryset)
        return Response(
            data=serializer_data.data,
            status=status.HTTP_200_OK
        )
    
    def partial_update(self, request, pk):
        queryset = get_object_or_404(self.queryset, pk=pk)
        serializer_data = self.serializer_class(instance = queryset, data=request.data, partial=True)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(
                data = serializer_data.data,
                status= status.HTTP_200_OK
            )
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk):
        queryset = get_object_or_404(self.queryset, pk=pk)
        queryset.delete()
        return Response({"message":"Deleted successfuly"}, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer_data = self.serializer_class(data = request.data)
        if serializer_data.is_valid():
            serializer_data.create(serializer_data.validated_data)
            return Response(
                data = serializer_data.data,
                status= status.HTTP_201_CREATED
            )
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)

class HotelViewSet(viewsets.ViewSet):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.filter(active=True)

    def list(self, request):
        serializer_data = self.serializer_class(instance=self.queryset.all(), many=True)
        return Response(
            data=serializer_data.data,
            status=status.HTTP_200_OK
        )
    
    def retrieve(self, request, pk):
        queryset = get_object_or_404(self.queryset, slug=pk)
        serializer_data = self.serializer_class(instance = queryset)
        return Response(
            data=serializer_data.data,
            status=status.HTTP_200_OK
        )
    
    def destroy(self, request, pk):
        if request.user.is_superuser:
            queryset = get_object_or_404(self.queryset, pk=pk)
            queryset.delete()
            return Response({"message":"Deleted successfuly"}, status=status.HTTP_200_OK)
        return Response({"message":"Forbidden!!!"}, status=status.HTTP_403_FORBIDDEN)

class CreateHotelAPIView(APIView):
    permission_classes = [IsAdminUser,]
    serializer_class = CreateUpdateHotelSerializer

    def post(self, request):
        serializer_data = self.serializer_class(data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(
                data = serializer_data.data,
                status= status.HTTP_201_CREATED
            )
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateHotelAPIView(APIView):
    permission_classes = [IsAdminUser,]
    serializer_class = CreateUpdateHotelSerializer

    def put(self, request, hotel_id):
        hotel = get_object_or_404(Hotel, id = hotel_id)
        serializer_data = self.serializer_class(instance=hotel, data=request.data, partial=True)

        if serializer_data.is_valid():
            serializer_data.save()
            return Response(
                data = serializer_data.data,
                status= status.HTTP_200_OK
            )
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
class HotelGaleryViewSet(viewsets.ViewSet):
    permission_classes = [IsAdminUser,]
    serializer_class = HotelGalerySerializer
    queryset = HotelGalery.objects.all()

    def list(self, request):
        serializer_data = self.serializer_class(instance=self.queryset.all(), many=True)
        return Response(
            data=serializer_data.data,
            status=status.HTTP_200_OK
        )
    
    def retrieve(self, request, pk):
        queryset = get_object_or_404(self.queryset, pk=pk)
        serializer_data = self.serializer_class(instance=queryset)
        return Response(
            data=serializer_data.data,
            status=status.HTTP_200_OK
        )
    
    def destroy(self, request, pk):
        queryset = get_object_or_404(self.queryset, pk=pk)
        queryset.delete()
        return Response({"message":"Deleted successfuly"}, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer_data = self.serializer_class(data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(
                data = serializer_data.data,
                status= status.HTTP_201_CREATED
            )
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RoomGaleryViewSet(viewsets.ViewSet):
    permission_classes = [IsAdminUser,]
    serializer_class = RoomGalerySerializer
    queryset = RoomGalery.objects.all()

    def list(self, request):
        serializer_data = self.serializer_class(instance=self.queryset.all(), many=True)
        return Response(
            data=serializer_data.data,
            status=status.HTTP_200_OK
        )
    
    def retrieve(self, request, pk):
        queryset = get_object_or_404(self.queryset, pk=pk)
        serializer_data = self.serializer_class(instance=queryset)
        return Response(
            data=serializer_data.data,
            status=status.HTTP_200_OK
        )
    
    def destroy(self, request, pk):
        queryset = get_object_or_404(self.queryset, pk=pk)
        queryset.delete()
        return Response({"message":"Deleted successfuly"}, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer_data = self.serializer_class(data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(
                data = serializer_data.data,
                status= status.HTTP_201_CREATED
            )
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)




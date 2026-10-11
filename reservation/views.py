from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from hotels.models import Room
from .models import Bespeak
from .serializers import (
    BespeakSerializer, 
    CreateBespeakSerializer
)


class BespeakViewSet(ViewSet):
    permission_classes = [IsAdminUser,]
    serializer_class = BespeakSerializer
    queryset = Bespeak.objects.all()

    def list(self, request):
        serializer_data = self.serializer_class(instance = self.queryset.all(), many = True)
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
    
    def destroy(self, request, pk):
        queryset = get_object_or_404(self.queryset, pk=pk)
        queryset.delete()
        return Response({"message":"Deleted successfuly"})

class CreateBespeakAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = CreateBespeakSerializer

    def post(self, request, room_id):
        room = get_object_or_404(Room, id=room_id)
        serializer_data = self.serializer_class(data = request.data)

        if serializer_data.is_valid():
            user = request.user
            vd = serializer_data.validated_data
            if room.available:
                bespeak =Bespeak.objects.create(
                    user = user,
                    room = room,
                    arrival_time = vd["arrival_time"],
                    exit_time = vd["exit_time"],
                    gender = vd["gender"],
                    manager = vd["manager"],
                    nationality = vd["nationality"],
                    national_code = vd["national_code"],
                    additional_request = vd["additional_request"],
                    reserved = True
                )
                bespeak.room.available = False
                bespeak.room.save()
                return Response(
                    data=serializer_data.data,
                    status=status.HTTP_200_OK
                )
            else:
                return Response({"message":"the hotel allready reserved"},status=status.HTTP_400_BAD_REQUEST)   
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)
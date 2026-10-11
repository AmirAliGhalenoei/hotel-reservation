from django.urls import path
from .import views
from rest_framework import routers

urlpatterns = [
    path("add/hotel/",views.CreateHotelAPIView.as_view()),
    path("update/hotel/<int:hotel_id>/",views.UpdateHotelAPIView.as_view()),
]

router = routers.SimpleRouter()
router.register("hotels", views.HotelViewSet)
router.register("hotel-galery", views.HotelGaleryViewSet)
router.register("room-galery", views.RoomGaleryViewSet)
router.register("cities", views.CityViewSet)
router.register("facilitys", views.FacilityViewSet)
urlpatterns += router.urls
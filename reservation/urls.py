from django.urls import path
from .import views
from rest_framework import routers

urlpatterns = [
    path("reserve/<int:room_id>/",views.CreateBespeakAPIView.as_view()),
]

router = routers.SimpleRouter()
router.register("reservation",views.BespeakViewSet)
urlpatterns += router.urls
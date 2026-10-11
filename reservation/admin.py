from django.contrib import admin
from .models import Bespeak


@admin.register(Bespeak)
class BespeakAdmin(admin.ModelAdmin):
    list_display = ["user", "phone", "manager", "hotel", "room", "arrival_time", "exit_time", "asking_price", "reserved"]
    list_filter = ["reserved"]
    search_fields = ["national_code"]

    def hotel(self, obj):
        return obj.room.hotel
    def phone(self, obj):
        return obj.user.phone

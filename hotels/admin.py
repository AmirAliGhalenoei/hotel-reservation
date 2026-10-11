from django.contrib import admin
from .models import (
    Room,
    Hotel, 
    Cities, 
    RoomGalery,
    HotelGalery,
    RoomFacility, 
    HotelFacility,   
)


@admin.register(Cities)
class CitiesAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "id"]

@admin.register(HotelFacility)
class HotelFacilityAdmin(admin.ModelAdmin):
    list_display = ["title", "id"]

@admin.register(RoomFacility)
class RoomFacilityAdmin(admin.ModelAdmin):
    list_display = ["title", "id"]

class HotelGaleryInlines(admin.TabularInline):
    model = HotelGalery
class RoomGaleryInlines(admin.TabularInline):
    model = RoomGalery
class RoomInlines(admin.TabularInline):
    model = Room
@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ["name", "star", "active", "id"]
    search_fields = ["name"]
    list_filter = ["active"]
    inlines = [RoomInlines, RoomGaleryInlines, HotelGaleryInlines]
    filter_horizontal = ("facilitys",)
    

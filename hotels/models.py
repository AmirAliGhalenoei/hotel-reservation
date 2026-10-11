from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Cities(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60)

    def __str__(self):
        return self.name
    
class HotelGalery(models.Model):
    hotel = models.ForeignKey("Hotel", on_delete=models.CASCADE,related_name="galerys")
    image = models.ImageField(upload_to=f"images/galerys/{hotel.name}/")

class RoomGalery(models.Model):
    hotel = models.ForeignKey("Hotel", on_delete=models.CASCADE, related_name="room_galerys")
    room = models.ForeignKey("Room", on_delete=models.CASCADE)
    image = models.ImageField(upload_to=f"images/galerys/rooms/{room.name}/")

    def __str__(self):
        return str(self.room)

class HotelFacility(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class RoomFacility(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Hotel(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60, unique=True)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, related_name="hotels")
    description = models.TextField()
    facilitys = models.ManyToManyField(HotelFacility, related_name="hotel_facilitys")
    address = models.TextField()
    star = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(6)])
    website = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to="images/baners/", null=True, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="rooms")
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=60, unique=True)
    facilitys = models.ManyToManyField(RoomFacility, related_name="room_facilitys")
    rooms = models.IntegerField()
    soldiers = models.IntegerField()
    available = models.BooleanField(default=True)
    price = models.DecimalField(decimal_places=0, max_digits=12)

    def __str__(self):
        return self.name
    




    
from django.db import models
from django.core.validators import validate_integer
from .validators import national_code_validator
from hotels.models import Room
from accounts.models import User


class Bespeak(models.Model):

    NATIONALITY = [
        ("iran","ایرانی"),
        ("other","خارجی"),
    ]

    GENDER = [
        ("man","مرد"),
        ("woman","زن"),
    ]

    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="user_bespeak")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="booking")
    arrival_time = models.DateField()
    exit_time = models.DateField()
    gender = models.CharField(max_length=5,choices=GENDER)
    manager = models.CharField(max_length=100)
    nationality = models.CharField(max_length=5,choices=NATIONALITY)
    national_code = models.CharField(max_length=10, validators=[validate_integer,national_code_validator])
    additional_request = models.TextField(null=True, blank=True)
    reserved = models.BooleanField(default=False)
    asking_price = models.DecimalField(decimal_places=0, max_digits=12, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.asking_price = (self.exit_time - self.arrival_time).days * self.room.price
        return super().save(*args, **kwargs)
    

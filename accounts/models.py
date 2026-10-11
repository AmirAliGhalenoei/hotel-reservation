from django.db import models
from django.core.validators import validate_integer, validate_email
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
from .validators import validate_iranian_phone
import uuid


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = models.CharField(max_length=11,unique=True,validators=[validate_integer,validate_iranian_phone],db_index=True)
    email = models.EmailField(max_length=60, unique=True, validators=[validate_email], null=True, blank=True)
    first_name = None
    last_name = None
    
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["username", "email"]

    objects = UserManager()

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.username
    


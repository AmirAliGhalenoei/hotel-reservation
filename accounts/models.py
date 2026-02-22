from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin
from django.core.validators import validate_integer , validate_email
from .managers import UserManager
from .validators import validate_iranian_phone
# Create your models here.
import uuid


class User(PermissionsMixin, AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = models.CharField(max_length=11,unique=True,validators=[validate_integer,validate_iranian_phone],db_index=True)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=60, unique=True, validators=[validate_email])
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["username", "email"]

    objects = UserManager()

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj = None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
    
    

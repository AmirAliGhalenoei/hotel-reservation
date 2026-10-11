from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.validators import validate_integer
from .validators import validate_iranian_phone


class UserCreationForm(UserCreationForm):
    phone = forms.CharField(max_length=11,validators=[validate_integer, validate_iranian_phone])

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ("phone",)
    
    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if User.objects.filter(phone = phone).exists():
            raise ValidationError("phone number allready exists")
        return phone
  
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("phone", "username", "email", "password")


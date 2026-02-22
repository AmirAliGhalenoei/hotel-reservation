from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    password = forms.CharField()
    conform_password = forms.CharField()

    class Meta:
        fields = ("phone", "username", "email")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    def clean_conform_password(self):
        cd = self.cleaned_data
        if cd["password"] and cd["conform_password"] and cd["password"] != cd["conform_password"]:
            raise ValidationError("The passwords do not match.")
        return cd["conform_password"]
    

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        fields = ("phone", "username", "email", "password","updated")


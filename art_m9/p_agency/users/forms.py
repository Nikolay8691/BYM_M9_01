from django.contrib.auth.forms import UserCreationForm

from django import forms
from .models import Profile

# Create your forms here.
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name',)

class ProfileForm2(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('nick', 'phone')

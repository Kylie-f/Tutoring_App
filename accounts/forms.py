from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser, Availability, Class, Tutor

class CustomUserCreationForm(UserCreationForm):
        classes = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter classes separated by commas'}),
        required=False,
        label="Classes you want to tutor"  # Optional label for clarity
    )
        class Meta:
            model = CustomUser
            fields = ('username', 'email', 'password1', 'password2', 'classes')  # Explicitly list all required fields

class CustomUserChangeForm(UserChangeForm):
    classes = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter classes separated by commas'}),
        required=False,
        label="Classes you want to tutor"  # Optional label for clarity
    )

    class Meta:
        model = CustomUser
        fields = tuple(UserCreationForm.Meta.fields) + ("classes",)


class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ['day', 'start_time', 'end_time']

class TutorEditForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['name', 'email', 'classes_tutored', 'major', 'fun_fact', 'description', 'monday_hours', 'available_hours'] 
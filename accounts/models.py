from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# New model to represent classes
class Class(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Extending the default user model to include classes the user can tutor
class CustomUser(AbstractUser):
    classes = models.ManyToManyField(Class, blank=True)  # Users can select multiple classes

# Model for Tutors
class Tutor(models.Model):
    name = models.CharField(max_length=255)  # Name of the tutor
    email = models.EmailField(unique=True)  # Email for the tutor
    # Removed the `classes` CharField; it was unnecessary
    classes_tutored = models.CharField(max_length=255, blank=True)  # Make this optional
    major = models.CharField(max_length=100, default="Undeclared")
    fun_fact = models.CharField(max_length=200, default="No fun fact available")  # Set a default value
    description = models.TextField()
    monday_hours = models.TextField(null=True, blank=True)
    available_hours = models.IntegerField(default=0)  # Or whatever field type is appropriate

    def __str__(self):
        return f"{self.name} - Classes: {self.classes_tutored or 'None'}"

# Availability model to track tutor availability
class Availability(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Linked to CustomUser
    day = models.CharField(max_length=10)  # e.g., 'Monday'
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.user.username} - {self.day}: {self.start_time} to {self.end_time}"

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Tutor, Availability

# CustomUserAdmin to manage CustomUser model
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("classes",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("classes",)}),)

# Register Tutor model for the admin site
class TutorAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "classes_tutored"]  # Include fields you want to display
    fields = ["name", "email", "classes_tutored", "major", "fun_fact", "description", "monday_hours", "available_hours"]  # Ensure `classes` is not listed here

# Register Availability model for the admin site
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ["user", "day", "start_time", "end_time"]

# Register all models with the admin site
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Tutor, TutorAdmin)
admin.site.register(Availability, AvailabilityAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('phone_number', 'full_name', 'address', 'gender', 'is_staff')
    list_display_links = ()


admin.site.register(User, CustomUserAdmin)




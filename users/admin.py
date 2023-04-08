from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, House, Travel
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('phone_number', 'full_name', 'address', 'gender', 'is_staff')
    list_display_links = ('phone_number', 'full_name')
    list_filter = ('address', 'gender')
    search_fields = ('phone_number', 'full_name', 'address', 'gender')


admin.site.register(User, CustomUserAdmin)


class HouseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'rent_house', 'rent_contract', 'location')
    list_display_links = ('title', 'price')
    list_filter = ('rent_house', 'rent_contract', 'price')
    search_fields = ('title', 'location')


admin.site.register(House, HouseAdmin)


class TravelAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    list_display_links = ('name', 'address')
    list_filter = ('name', )
    search_fields = ('name', 'address')


admin.site.register(Travel, TravelAdmin)

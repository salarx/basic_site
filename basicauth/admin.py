from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import EditProfileForms
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    #add_form = CustomUserCreationForm
    form = EditProfileForms
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name','email', 'college_name', 'password',]

admin.site.register(CustomUser, CustomUserAdmin)

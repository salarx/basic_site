from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import SignUpForms
from .forms import EditProfileForms
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = SignUpForms
    form = EditProfileForms
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name','email', 'password', 'college_name']

admin.site.register(CustomUser, CustomUserAdmin)

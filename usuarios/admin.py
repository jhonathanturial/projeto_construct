from django.contrib import admin
from .models import Users
from django.contrib.auth import admin as admin_auth_django
from .forms import UserChangeForm, UserCreationForm

@admin.register(Users)
class UsersAdmin(admin_auth_django):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Users
# Register your models here.

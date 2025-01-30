from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Ruyxat
# Register your models here.
class AdminPanel(admin.ModelAdmin):
    list_display = ['first_name', 'tell', 'add_time'] 
admin.site.register(Ruyxat, AdminPanel)
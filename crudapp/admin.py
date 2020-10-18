from django.contrib import admin
from .models import student, User

# Register your models here.
@admin.register(student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'mobile', 'password')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    User_display = ('username123','password123')

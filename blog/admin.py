from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "password")
    list_display_links = ("id", "username", "password")
    list_filter = ("username","created_at")


admin.site.register(User,UserAdmin)

from django.contrib import admin

from user.models import UserModel


# Register your models here.
@admin.site.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name')

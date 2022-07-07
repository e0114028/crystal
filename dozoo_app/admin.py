from django.contrib import admin
from .models import Message,Friend,Group,Good,User

from django.contrib.auth.admin import UserAdmin



# Register your models here.
admin.site.register(Message)
admin.site.register(Friend)
admin.site.register(Group)
admin.site.register(Good)


class CustomUserAdmin(UserAdmin):
    list_display = list(UserAdmin.list_display) + ['custom_field']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('custom_field',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('custom_field',)}),
    )

# admin.site.register(User, UserAdmin)
# # fieldを追加した場合は下
admin.site.register(User,CustomUserAdmin)
admin.site.unregister(User)
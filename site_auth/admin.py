# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser

# admin.site.register(CustomUser, UserAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, CustomGroup, CustomSite
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
# import django.contrib.auth.models

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'site', 'first_name', 'last_name', 'is_staff', 'is_active',)
    list_filter = ('email', 'site', 'first_name', 'last_name', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.unregister(Group)
admin.site.unregister(Site)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomGroup)
admin.site.register(CustomSite)
# admin.site.register(CustomUser, UserAdmin)


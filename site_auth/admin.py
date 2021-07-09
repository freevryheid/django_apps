from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, CustomGroup, CustomSite
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'site', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_active',)
    list_filter = ('email', 'site', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'password')}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_superuser', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


# class ForeignKeyFilter(object):
#     def formfield_for_dbfield(self, db_field, **kwargs):
#         # Only show the foreign key objects from the rendered filter.
#         filters = getattr(self, 'foreignkey_filters', None)
#         if filters and db_field.name in filters:
#             kwargs['queryset'] = filters[db_field.name](Site.objects.get_current())
#         return admin.ModelAdmin.formfield_for_dbfield(self, db_field, **kwargs)


# class SiteOnlyAdmin(ForeignKeyFilter, admin.ModelAdmin):
#     foreignkey_filters = {
#       'site' : lambda site : Site.objects.filter(name=site.name)
#     }


admin.site.unregister(Group)
admin.site.unregister(Site)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomGroup)
admin.site.register(CustomSite)



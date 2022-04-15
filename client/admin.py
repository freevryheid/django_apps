from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, CustomGroup, CustomSite
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import PasswordResetForm
# from django.utils.crypto import get_random_string

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        pwd = CustomUser.objects.make_random_password(length=14)
        self.fields['password1'].initial = pwd
        self.fields['password2'].initial = pwd
        self.fields['password1'].widget.render_value = True
        self.fields['password2'].widget.render_value = True

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email_user(subject="I2MS Access", message=self.cleaned_data["password1"])
        # messages.info('Email sent to user.')
        if commit:
            user.save()
        return user

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    list_display = ('email', 'site', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_active',)
    list_filter = ('email', 'site', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'site', 'first_name', 'last_name', 'password')}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'site', 'first_name', 'last_name', 'password1', 'password2', 'is_superuser', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.unregister(Group)
admin.site.unregister(Site)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomGroup)
admin.site.register(CustomSite)






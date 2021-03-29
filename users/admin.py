from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Users
from .forms import UserCreationForm, UserChangeForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'username', 'email', 'nome', 'ativo', 'is_active',)
    list_display_links = ('id', 'username', 'email',)
    list_editable = ('ativo', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'first_name',
                                      'last_name', 'instit', 'idpescod', 'idgrp')}),
        ('Permissions', {
         'fields': ('is_active', 'ativo', 'acess')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('short',),
            'fields': ('username', 'password1', 'password2',)
        }),
        ('Personal info', {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'instit', 'idpescod', 'idgrp', 'ativo', 'acess')
        }),
    )
    search_fields = ('username', 'first_name')
    ordering = ('username',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(Users, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)

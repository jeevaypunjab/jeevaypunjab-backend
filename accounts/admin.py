from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from .models import UserProfile
from .forms import UserProfileForm


class UserProfileAdmin(admin.StackedInline):
    model = UserProfile
    form = UserProfileForm
    fields = ('profile_photo', 'phone_number', 'about', 'facebook',
              'instagram')


class UserAdmin(DjangoUserAdmin):
    inlines = [UserProfileAdmin]
    fieldsets = ((
        _('Personal info'), {
            'fields': ('username', 'first_name', 'last_name', 'email',
                       'password')
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups',
                       'user_permissions')
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name',
                    'date_joined',)
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('first_name',)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

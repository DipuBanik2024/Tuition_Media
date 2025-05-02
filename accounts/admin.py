from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Qualification

class UserAdmin(BaseUserAdmin):
    # Fields to show in admin list view
    list_display = ('name', 'email', 'phone', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active', 'gender')

    # Fields visible in detail (edit) view
    fieldsets = (
        (None, {'fields': ('email', 'phone', 'password')}),
        ('Personal Info', {'fields': ('name', 'role', 'gender', 'district', 'location', 'preferred_area', 'profile_picture')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    # Fields when creating a new user (add form)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone', 'name', 'role', 'gender', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )

    search_fields = ('email', 'phone', 'name')
    ordering = ('email',)

# Qualification model simple admin
class QualificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'degree', 'result', 'year', 'institute')
    search_fields = ('user__name', 'degree', 'institute')
    list_filter = ('degree', 'year')

# Register models to admin site
admin.site.register(User, UserAdmin)
admin.site.register(Qualification, QualificationAdmin)

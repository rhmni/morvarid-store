from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .forms import UserCreateForm, UserEditForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserEditForm
    add_form = UserCreateForm
    list_display = ['email', 'id', 'is_active', 'is_superuser']
    list_filter = ['is_active', 'is_superuser', 'last_login', 'join_date']
    search_fields = ['email', 'first_name', 'last_name', 'phone', 'code_meli', 'address', 'shahr', 'ostan']
    ordering = ('-id',)
    filter_horizontal = ()
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('اطلاعات شخصی', {'fields': ('first_name', 'last_name', 'phone', 'avatar')}),
        ('مجوزها', {'fields': ('is_active', 'is_superuser')}),
        ('اطلاعات گیرنده', {'fields': ('code_meli', 'ostan', 'shahr', 'address')}),
        ('تاریخ های مهم', {'fields': ('last_login', 'join_date')}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'password', 'password2')}),
    )


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

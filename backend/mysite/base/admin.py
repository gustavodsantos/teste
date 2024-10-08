from django.contrib import admin
from django_min_custom_user.admin import MinUserAdmin

from mysite.base.models import User


@admin.register(User)
class UserAdmin(MinUserAdmin):
    pass

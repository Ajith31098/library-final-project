from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user_app.models import User, MemberShip

# Register your models here.

fields = list(UserAdmin.fieldsets)
fields[1] = ('Personal Info', {'fields': (
    'first_name', 'last_name', 'email', 'usertype')})
UserAdmin.fieldsets = tuple(fields)

admin.site.register(User, UserAdmin)
admin.site.register(MemberShip)

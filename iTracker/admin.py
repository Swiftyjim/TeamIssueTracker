from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.


admin.site.register(Project)
admin.site.register(Team)

class UserExtendedInline(admin.StackedInline):
    model = UserExtended
    cen_delete= False
    verbose_name_plural = 'User_Extended'

class CustomizedUserAdmin(UserAdmin):
    inlines=(UserExtendedInline,)

admin.site.unregister(User)
admin.site.register(User,CustomizedUserAdmin)
from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile

from campaigns.models import Campaign, Supervisor, House, Checkup, Apartment, CheckupResults

# Register your models here.
class ProfileInline(admin.StackedInline):
	model = Profile 
	can_delete = False
	verbose_name_plural = 'profile'

class UserAdmin(BaseUserAdmin):
	inlines = (ProfileInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Supervisor)
admin.site.register(Campaign)
admin.site.register(House)
admin.site.register(Checkup)
admin.site.register(Apartment)
admin.site.register(CheckupResults)
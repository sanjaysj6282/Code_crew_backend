
from django.contrib import admin

from .models import userDetails

admin.site.register(userDetails)

# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User

# from .models import userDetails

# class userInline(admin.StackedInline):
#     model = userDetails
#     can_delete = False
#     verbose_name_plural = 'userProfile'

# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = [userInline]

# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
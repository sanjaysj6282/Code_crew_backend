from django.contrib import admin

from .models import userDetails

# admin.site.register(userDetails)

class ClientDetailsAdmin(admin.ModelAdmin):
    def get_changeform_initial_data(self, request):
        get_data = super(ClientDetailsAdmin, self).get_changeform_initial_data(request)
        get_data['created_by'] = request.user.pk
        return get_data

admin.site.register(userDetails, ClientDetailsAdmin)

# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User

# from .models import userDetails

# # Define an inline admin descriptor for Employee model
# # which acts a bit like a singleton
# class userInline(admin.StackedInline):
#     model = userDetails
#     can_delete = False
#     verbose_name_plural = 'userProfile'

# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = [userInline]

# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
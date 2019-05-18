from django.contrib import admin
from .models import User,AddressBook
from authemail.admin import EmailUserAdmin

class MyUserAdmin(EmailUserAdmin):
    fieldsets = (
        (None, {
            "fields": (
                'first_name','last_name','email','date_of_birth','phoneno','image','is_seller'
            ),
        }),
    )
    

admin.site.unregister(User)
admin.site.register(User,MyUserAdmin)
admin.site.register(AddressBook)
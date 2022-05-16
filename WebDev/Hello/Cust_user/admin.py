from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserData
# Register your models here.


class CustomUserAdmin(UserAdmin):

    list_display = (
        'username', 'password','first_name', 'last_name', 'email',
        'res1', 'res2', 'res3','res4', 'res5', 'rate1', 'rate2','rate3','rate4','rate5'
        )

    fieldsets = (
       
        ('Personal info', {
            'fields': ('username', 'password','first_name', 'last_name', 'email')
        }),
        ('Restaurants', {
            'fields': (
                'res1', 'res2', 'res3',
                'res4', 'res5'
                )
        }),
        ('Rating', {
            'fields': ('rate1', 'rate2','rate3','rate4','rate5')
        }),
        
    )

admin.site.register(UserData, CustomUserAdmin)
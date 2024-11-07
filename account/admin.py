from django.contrib import admin
from .models import UserAccount, Post

# Register your models here.
class UserAccountAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'firstname',
        'lastname',
    ]
    search_fields=[
        'firstname',
        'lastname',
    ]
    
class PostAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'title',
    ]
    search_fields=[
        'title',
    ]

admin.site.register(UserAccount, UserAccountAdmin) 
admin.site.register(Post, PostAdmin) 

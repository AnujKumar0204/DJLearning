from django.contrib import admin
from django.utils.html import format_html
from .models import *

# Register your models here.
class UserAccountAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'username',
        'firstname',
        'lastname',
    ]
    search_fields=[
        'username',
        'firstname',
        'lastname',
    ]
    readonly_fields = ['password']
    
class PostAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'user_link',
        'title',
    ]
    search_fields=[
        'title',
    ]
    
    def user_link(self, obj) :
        return format_html( f'<a href="/admin/account/useraccount/{obj.user.id}/" >{obj.user.username}</a>' )


class InterestCategoryAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'name',
    ]
    search_fields=[
        'name',
    ]
    
class InterestAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'category_link',
        'name',
    ]
    search_fields=[
        'name',
        'category',
    ]
    list_filter=[
        'category',
    ]
    
    def category_link(self, obj) :
        return format_html( f'<a href="/admin/account/interestcategory/{obj.category.id}/" >{obj.category.name}</a>' )
    
class UserInterestMapAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'user_link',
        'interest_link',
    ]
    search_fields=[
        'user',
        'interest',
    ]
    
    def user_link(self, obj) :
        return format_html( f'<a href="/admin/account/useraccount/{obj.user.id}/" >{obj.user.username}</a>' )
    
    def interest_link(self, obj) :
        return format_html( f'<a href="/admin/account/interest/{obj.interest.id}/" >{obj.interest.name}</a>' )


admin.site.register(UserAccount, UserAccountAdmin) 
admin.site.register(Post, PostAdmin) 
admin.site.register(InterestCategory, InterestCategoryAdmin) 
admin.site.register(Interest, InterestAdmin) 
admin.site.register(UserInterestMap, UserInterestMapAdmin) 

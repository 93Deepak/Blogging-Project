from django.contrib import admin
from blogapp.models import Users
from blogapp.models import Blogs

class UsersAdmin(admin.ModelAdmin):
    list_display=['name','mobile','email','password','dob']

admin.site.register(Users,UsersAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display=['title','blog','author','upload_date']

admin.site.register(Blogs,BlogAdmin)

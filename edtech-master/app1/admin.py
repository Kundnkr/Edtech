from django.contrib import admin
from .models import User,Profile,ManageCategory,EducationLevel

# Register your models here.



class UserAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email','phone','password']

admin.site.register(User,UserAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','name','locality','city','zipcode','state']

admin.site.register(Profile,ProfileAdmin)



class ManageCategoryAdmin(admin.ModelAdmin):
    list_display = ['title','selling_price','description','sub_category','category','product_image']

admin.site.register(ManageCategory,ManageCategoryAdmin)


class EducationAdmin(admin.ModelAdmin):
    list_display = ['education','study_field','university','college','country','city','state']

admin.site.register(EducationLevel,EducationAdmin)

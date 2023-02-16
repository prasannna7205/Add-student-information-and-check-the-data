from django.contrib import admin
from displayapp.models import UserData

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['name','last_name','salary','address']
admin.site.register(UserData,EmployeeAdmin)

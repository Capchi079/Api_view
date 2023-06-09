from django.contrib import admin

# Register your models here.
from app.models import *





class ProductAdmin(admin.ModelAdmin):
    list_display=['Pid','Pname','Pprice','Pdescription','Pdate' ]

admin.site.register(Product_Catagory)
admin.site.register(Product,ProductAdmin)
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.conf import settings
from product.models import product, product_type, product_category
#from sorl.thumbnail.admin import AdminImageMixin
# Register your models here.

class product_category_admin(admin.ModelAdmin):
    list_display = ('name',)

class product_type_admin(admin.ModelAdmin):
    list_display = ('product_category','name',)

class product_admin(admin.ModelAdmin):
    list_display = ('product_type','name','description','price')
    readonly_fields=('pid',)

    #def get_category(self,obj):
     #   return obj.product_type.product_category


admin.site.register(product_category,product_category_admin)
admin.site.register(product_type,product_type_admin)
admin.site.register(product,product_admin)

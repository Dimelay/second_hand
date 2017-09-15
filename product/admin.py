# -*- coding: utf-8 -*-

from django.contrib import admin
from django.conf import settings
from product.models import discont,product, product_type, product_category
#from sorl.thumbnail.admin import AdminImageMixin
# Register your models here.

class product_category_admin(admin.ModelAdmin):
    list_display = ('name',)

class discont_admin(admin.ModelAdmin):
    list_display = ('name','procent',)


class product_type_admin(admin.ModelAdmin):
    list_display = ('product_category','name',)

class product_admin(admin.ModelAdmin):
    list_display = ('get_thum_128','product_type','name','description','price','sold','print_barcode')
    readonly_fields=('pid',)
    search_fields = ('name','description')
    list_filter=('sold',)
    list_per_page = 20

    def get_readonly_fields(self, request, obj=None):
        self.readonly_fields = ('pid',)
        if obj and obj.sold == True:
            self.readonly_fields = [field.name for field in obj.__class__._meta.fields]
        return self.readonly_fields

    def print_barcode(self,obj):
        return u'<a target=_blank href=/print_barcode/%s/>Напечатать ценник</a>' % (obj.pid)
    print_barcode.allow_tags = True
    #def get_category(self,obj):
     #   return obj.product_type.product_category

admin.site.register(discont,discont_admin)
admin.site.register(product_category,product_category_admin)
admin.site.register(product_type,product_type_admin)
admin.site.register(product,product_admin)

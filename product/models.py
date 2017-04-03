# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

import datetime,time,os
import PIL
from PIL import Image
from django.conf import settings
#from sorl.thumbnail import ImageField, get_thumbnail
#from sorl.thumbnail import ImageField
# Create your models here.

class product_category(models.Model):
    class Meta:
        verbose_name_plural = 'Категория товара'
        verbose_name = 'Категория товара'

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=250, verbose_name='Категория товара')

class product_type(models.Model):
    class Meta:
        verbose_name_plural = 'Вид товара'
        verbose_name = 'Вид товара'

    def __unicode__(self):
        return '%s - %s' % (self.product_category,self.name)

    name = models.CharField(max_length=250, verbose_name='Вид товара')
    product_category = models.ForeignKey('product_category',verbose_name='Категория товара', default=None, null=True, on_delete=models.SET_NULL)

def gen_pid():
    return time.mktime(datetime.datetime.now().timetuple())

class sale_log(models.Model):
    product_id = models.ForeignKey('product')
    user_id = models.ForeignKey(User)
    dates = models.DateTimeField(default=datetime.datetime.now())
    money_in = models.IntegerField(default=0)
    money_out = models.IntegerField(default=0)
    action = models.CharField(max_length=255)

class product(models.Model):
    class Meta:
        permissions = (
            ('print_barcode','Печать ценников'),
        )
        verbose_name_plural = 'Товар'
        verbose_name = 'Товар'

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=250,verbose_name='Название')
    in_date = models.DateTimeField(verbose_name='Дата привоза', default=datetime.datetime.now())
    out_date = models.DateTimeField(verbose_name='Дата продажи', default=datetime.datetime.now(),null=True, blank=True, editable=False)
    pid = models.CharField(max_length=50,verbose_name='Артикул', unique=True, default=gen_pid,editable=False)
    price = models.IntegerField(verbose_name='Цена')
    photo = models.ImageField(upload_to='photo',verbose_name='Фото')
    description = models.CharField(max_length=255,null=True,verbose_name='Краткое описание')
    product_type = models.ForeignKey('product_type',verbose_name='Вид товара', default=None, null=True, on_delete=models.SET_NULL)
    sold = models.BooleanField(default=False, editable=False)
    def save(self, *args, **kwargs):
       if self.photo:
            #self.photo = get_thumbnail(self.photo, '640x480', quality=99, format='JPEG').url
            super(product, self).save(*args, **kwargs)
            basewidth = 256
            img = Image.open(os.path.join(settings.MEDIA_ROOT, self.photo.name))
            if img.mode not in ('L', 'RGB'):
                img = img.convert('RGB')
            wpercent = (basewidth / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
            img.save(os.path.join(settings.MEDIA_ROOT, self.photo.name))

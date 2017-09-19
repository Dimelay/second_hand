# -*- coding: utf-8 -*-
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from product.models import discont
from django.utils import timezone

from django.contrib.admin.widgets import AdminDateWidget

class discont_form(forms.Form):
   # discont = forms.ModelChoiceField(query=discont.objects.all(), widget=forms.RadioSelect)
    discont = forms.ModelChoiceField(label='Скидка',queryset=discont.objects.all(), to_field_name="procent", required=False, empty_label='Без скидки')

class date_input(forms.Form):
    class Media:
        js = ('js/print_barcode.js',)
    date_input = forms.DateField(initial=timezone.now,label=u'Дата ', widget=SelectDateWidget(attrs={'class':'date_input'},years=range(2016, 2030)))

class history_date_input(forms.Form):
    class Media:
        js = ('js/print_barcode.js',)
    #date_input = forms.DateField(initial=timezone.now,label=u'Дата ', widget=SelectDateWidget(attrs={'class':'date_input'},years=range(2016, 2030)))
    start_date = forms.DateField(label='Начало',widget=AdminDateWidget(format='SHORT_DATE_FORMAT'))
    end_date = forms.DateField(label='Конец',initial=timezone.now,widget=AdminDateWidget)
class SearchPoint(forms.Form):

	class Media:
		js = ('js/searchpoint.js',)
	pid = forms.CharField(widget=forms.TextInput(
		attrs={
		'autofocus':'on'
		}),
		label='Артикул', max_length=100)

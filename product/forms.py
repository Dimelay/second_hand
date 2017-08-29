# -*- coding: utf-8 -*-
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from product.models import discont
from django.utils import timezone

class discont_form(forms.Form):
   # discont = forms.ModelChoiceField(query=discont.objects.all(), widget=forms.RadioSelect)
    discont = forms.ModelChoiceField(label='Скидка',queryset=discont.objects.all(), to_field_name="procent", required=False, empty_label='Без скидки')

class date_input(forms.Form):
    class Media:
        js = ('js/print_barcode.js',)
    date_input = forms.DateField(initial=timezone.now,label=u'Дата ', widget=SelectDateWidget(attrs={'class':'date_input'},years=range(2016, 2030)))
class SearchPoint(forms.Form):

	class Media:
		js = ('js/searchpoint.js',)
	pid = forms.CharField(widget=forms.TextInput(
		attrs={
		'autofocus':'on'
		}),
		label='Артикул', max_length=100)

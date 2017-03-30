# -*- coding: utf-8 -*-
from django import forms
from django.forms.extras.widgets import SelectDateWidget
class PrintBarcodeByData(forms.Form):
    bar_date = forms.DateField(label=u'date of birth', widget=SelectDateWidget())
class SearchPoint(forms.Form):

	class Media:
		js = ('js/searchpoint.js',)
	pid = forms.CharField(widget=forms.TextInput(
		attrs={
		'autofocus':'on'
		}),
		label='Артикул', max_length=100)

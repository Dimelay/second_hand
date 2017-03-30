# -*- coding: utf-8 -*-
from django import template
register = template.Library()


@register.filter
def get_summ(log,s):
    a=0
    for i in log:
        if s=='in':
            a = a+i.money_in
        else:
            a = a+i.money_out
    return a

# -*- coding: utf-8 -*-
from django import template
register = template.Library()

@register.filter
def get_summ(log,s):
    a=0
    r_in=0
    r_out=0
    for i in log:
        if s=='in':
            a = a+i.money_in
        elif s=='out':
            a = a+i.money_out
        else:
            r_in = r_in+i.money_in
            r_out = r_out+i.money_out
            a = r_in - r_out
    return a

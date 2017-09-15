# -*- coding: utf-8 -*-
from django import template
from django.utils.safestring import mark_safe
register = template.Library()

@register.filter
def get_summ(log):
    stat = {}
    stat['money_in']=0
    stat['money_out']=0
    stat['money_all']=0
    for i in log:
        stat['money_in'] = stat['money_in']+i.money_in
        stat['money_out'] = stat['money_out']+i.money_out
        stat['money_all'] = stat['money_in']-stat['money_out']
    """
        if s=='in':
            a = a+i.money_in
        elif s=='out':
            a = a+i.money_out
        else:
            r_in = r_in+i.money_in
            r_out = r_out+i.money_out
            a = r_in - r_out
    """
    return mark_safe(('Приход: <b>%s</b> Расход: <b>%s</b> Итого: <b>%s</b>') % (stat['money_in'],stat['money_out'],stat['money_all']))

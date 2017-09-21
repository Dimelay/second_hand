# -*- coding: utf-8 -*-
from django import template
import datetime
from django.utils.safestring import mark_safe
from collections import OrderedDict
register = template.Library()

@register.inclusion_tag('history_result_tag.html')
def history_result(log):
    all_stat = {}
    all_money_in=0
    all_money_out=0
    all_money_all=0
    for i in log:
        all_money_in+=i.money_in
        all_money_out+=i.money_out
        d_date = datetime.datetime.strftime(i.dates.date(),"%Y-%m-%d")
        if d_date in all_stat:
            all_stat[d_date]['money_in']+=i.money_in
            all_stat[d_date]['money_out']+=i.money_out
            all_stat[d_date]['money_all']+=(i.money_in - i.money_out)
        else:
            all_stat[d_date]=dict(money_in=i.money_in,money_out=i.money_out,money_all=i.money_in-i.money_out)
    all_money_all = all_money_in - all_money_out
    all_stat[None]=dict(money_in=all_money_in,money_out=all_money_out,money_all=all_money_all)
    a=sorted(all_stat.items(), key=lambda x: x[0])
    return {'stat':a}

@register.filter
def to_datetime(val):
    try:
        return datetime.datetime.strptime(val,"%Y-%m-%d").date()
    except:
        return None

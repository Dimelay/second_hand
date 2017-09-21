# -*- coding: utf-8 -*-
from django import template
import datetime
from django.utils.safestring import mark_safe
from collections import OrderedDict
register = template.Library()

@register.inclusion_tag('history_result_tag.html')
def history_result(log):
    #all_stat = {}
    user_stat = {}
    all_money_in=0
    all_money_out=0
    all_money_all=0
    for i in log:
        all_money_in+=i.money_in
        all_money_out+=i.money_out
        d_date = datetime.datetime.strftime(i.dates.date(),"%Y-%m-%d")
        if d_date in user_stat:
            if i.user_id in user_stat[d_date]:
                user_stat[d_date][i.user_id]['money_in']+=i.money_in
                user_stat[d_date][i.user_id]['money_out']+=i.money_out
                user_stat[d_date][i.user_id]['money_all']+=(i.money_in - i.money_out)
            else:
                money_all = i.money_in - i.money_out
                user_stat[d_date][i.user_id]={'money_in':i.money_in,'money_out':i.money_out,'money_all':money_all}
        else:
            money_all = i.money_in - i.money_out
            user_stat[d_date]={i.user_id:{'money_in':i.money_in,'money_out':i.money_out,'money_all':money_all}}

        """
        if d_date in all_stat:
            all_stat[d_date]['money_in']+=i.money_in
            all_stat[d_date]['money_out']+=i.money_out
            all_stat[d_date]['money_all']+=(i.money_in - i.money_out)
        else:
            all_stat[d_date]=dict(money_in=i.money_in,money_out=i.money_out,money_all=i.money_in-i.money_out)
        """
    for i in user_stat:
        if len(user_stat[i]) > 1:
            total_user_money_in=0
            total_user_money_out=0
            total_user_money_all=0
            for users in user_stat[i]:
                total_user_money_in+=user_stat[i][users]['money_in']
                total_user_money_out+=user_stat[i][users]['money_out']
                total_user_money_all+=user_stat[i][users]['money_all']
            user_stat[i][None]={'money_in':total_user_money_in,'money_out':total_user_money_out,'money_all':total_user_money_all}

    all_money_all = all_money_in - all_money_out
    #all_stat[None]=dict(money_in=all_money_in,money_out=all_money_out,money_all=all_money_all)
    user_stat[None]={None:{'money_in':all_money_in,'money_out':all_money_out,'money_all':all_money_all}}
    user_stat=sorted(user_stat.items(), key=lambda x: x[0])
    #a=sorted(all_stat.items(), key=lambda x: x[0])
    #return {'stat':a,'user_stat':b}
    return {'user_stat':user_stat}

@register.filter
def to_datetime(val):
    try:
        return datetime.datetime.strptime(val,"%Y-%m-%d").date()
    except:
        return None

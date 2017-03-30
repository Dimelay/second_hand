# -*- coding: utf-8 -*-
from django.shortcuts import HttpResponse,render, redirect
#from django.template import loader, Context, RequestContext

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from product.models import product, sale_log
from product.forms import SearchPoint, PrintBarcodeByData
from django.http import Http404
import datetime

#from django.views.decorators import csrf
#from django.views.decorators.csrf import csrf_protect
# Create your views here.

def user_login(request):
	if request.method == 'POST':
            auth_form = AuthenticationForm(request, data=request.POST)
            if auth_form.is_valid():
                login(request,auth_form.get_user())
                return redirect("/")
            else:
                return render(request,'login2.html',{'auth_form':auth_form})
        else:
            auth_form = AuthenticationForm(None,None)
            return render(request,'login2.html',{'auth_form':auth_form})



@login_required(redirect_field_name=None)
def sale_product(request):
    err_list=[]
    if request.method == 'POST':
        reverse = request.POST.get('reverse')
        for i in request.POST.getlist("pid[]"):
            try:
                print reverse
                if reverse == '1':
                    pr = product.objects.get(pid=i,sold='1')
                    pr.sold = '0'
                    log = sale_log(product_id=pr,user_id=request.user,action='Возврат',money_out=pr.price)
                else:
                    pr = product.objects.get(pid=i,sold='0')
                    pr.sold = '1'
                    log = sale_log(product_id=pr,user_id=request.user,action='Продажа',money_in=pr.price)
                log.save()
                pr.save()
            except product.DoesNotExist:
                err_list.append(i)
                print err_list

    return HttpResponse('OK!')

@login_required(redirect_field_name=None)
def history(request):
    log = sale_log.objects.filter(dates__date=str(datetime.datetime.now())[:10],user_id=request.user)
    print log.all().count()
    return render(request,"history.html",{'log':log})

@login_required(redirect_field_name=None)
def get_product(request,pid,rev):
    print rev
    try:
        pr = product.objects.get(pid=pid,sold=rev)
    except product.DoesNotExist:
        raise Http404
    return render(request,"product.html",{'product':pr})

@login_required(redirect_field_name=None)
def get_barcode(request):
    if request.method == 'POST':
        bar_pid = PrintBarcodeByData(request.POST)
        print bar_pid.bar_date
    return HttpResponse('OK')

@login_required(redirect_field_name=None)
def user_logout(request):
	logout(request)
	return redirect("/")

@login_required(redirect_field_name=None)
def index(request):
	searchpoint = SearchPoint()
        barcodedate = PrintBarcodeByData()
        #log = get_log()
	return render(request,"main.html",{'searchpoint':searchpoint,'bd':barcodedate})

@login_required(redirect_field_name=None)
@permission_required('point.point_all_view',raise_exception=True)
def cart(request):
    return render(request,"cart.html",{'point': point.objects.exclude(fio='').order_by('fio') })

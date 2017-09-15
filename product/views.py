# -*- coding: utf-8 -*-
from django.shortcuts import HttpResponse,render, redirect
#from django.template import loader, Context, RequestContext

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.formats import get_format
from product.models import product, sale_log
from product.forms import discont_form,SearchPoint, date_input
from django.http import Http404
from bar import createBarCodes
import datetime, cups

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
        discont = request.POST.get('discont')
        for i in request.POST.getlist("pid[]"):
            try:
                #print reverse
                if reverse == '1':
                    pr = product.objects.get(pid=i,sold='1')
                    log = sale_log.objects.filter(product_id=pr,action='1').latest('dates')
                    pr.sold = '0'
                    log = sale_log(product_id=pr,user_id=request.user,action='0',money_out=log.money_in)
                else:
                    price = 0
                    pr = product.objects.get(pid=i,sold='0')
                    pr.sold = '1'
                    if discont:
                        d_discont = pr.price/100*int(discont)
                        price = pr.price - d_discont
                    else:
                        d_discont = 0
                        price = pr.price
                    log = sale_log(product_id=pr,user_id=request.user,action='1',money_in=price,discont=d_discont)
                log.save()
                pr.save()
            except product.DoesNotExist:
                err_list.append(i)
                #print err_list
    return HttpResponse('OK!')

@login_required(redirect_field_name=None)
def history(request):
    if request.method == 'GET':
        log = sale_log.objects.filter(dates__date=str(datetime.datetime.now())[:10],user_id=request.user).order_by('-dates')
    if request.method == 'POST':
        d_form = date_input(request.POST)
        if d_form.is_valid():
            #log = sale_log.objects.filter(dates__date=request.POST['start_date'],user_id=request.user)
            input_format = get_format('DATE_INPUT_FORMATS')[0]
            start_date = datetime.datetime.strptime(request.POST['start_date'],input_format)
            end_date = datetime.datetime.strptime(request.POST['end_date'],input_format)
            if request.user.has_perm('product.view_all'):
                log = sale_log.objects.filter(dates__range=(start_date,end_date))
            else:
                log = sale_log.objects.filter(dates__range=(start_date,end_date+datetime.timedelta(days=1)),user_id=request.user)
    return render(request,"history.html",{'log':log,'date_input': date_input()})
    #return render(request,"history.html",{'date_input':date_input()})


@login_required(redirect_field_name=None)
def get_product(request,pid,rev):
    #print rev
    try:
        pr = product.objects.get(pid=pid,sold=rev)
        if rev=='1':
            log = sale_log.objects.filter(product_id=pr,action='1').latest('dates')
            pr.price = log.money_in
    except product.DoesNotExist:
        raise Http404
    return render(request,"product.html",{'product':pr})

@login_required(redirect_field_name=None)
def print_barcode(request,pid):
    try:
        pr = product.objects.get(pid=pid)
        #response = HttpResponse(content_type='application/pdf')
        #response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
        #response.write(pdf)
    except product.DoesNotExist:
        raise Http404

    pdf = createBarCodes(pr)
    conn = cups.Connection()
    printers = conn.getPrinters()
    #for printer in printers:
     #   print printer, printers[printer]
    printer_name = printers.keys()[0]
    job_id = conn.createJob(printer_name, '', {})
    conn.startDocument(printer_name, job_id,'', cups.CUPS_FORMAT_RAW,1)
    conn.writeRequestData(pdf,len(pdf))
    conn.finishDocument(printer_name)
    #conn.printFile(printer_name,'/tmp/barcodes.pdf',"Python print",{})
    return HttpResponse('<script type=\"text/javascript\">self.close();</script>')

@login_required(redirect_field_name=None)
@permission_required('product.print_barcode',raise_exception=True)
def get_barcode(request):
    if request.method == 'GET':
        pr = False
        if request.GET:
            try:
                in_date = '%s-%s-%s' % (request.GET['date_input_year'],request.GET['date_input_month'],request.GET['date_input_day'])
                print in_date
                pr = product.objects.filter(in_date__date=in_date,sold='0')
                return render(request,"product_list.html",{'product':pr})
            except:
                pass
        return render(request,"bar.html",{'date_input':date_input()})
    if request.method == 'POST':
        bar_pid = date_input(request.POST)
        if bar_pid.is_valid():
            #print bar_pid.cleaned_data
            pr = product.objects.filter(in_date__date=str(bar_pid.cleaned_data['date_input']),sold='0')
            #for i in pr:
                #print i.name,i.pid,i.price
            pdf = createBarCodes(pr)
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
            response.write(pdf)
    return response

@login_required(redirect_field_name=None)
def user_logout(request):
	logout(request)
	return redirect("/")

@login_required(redirect_field_name=None)
def index(request):
	searchpoint = SearchPoint()
        discont = discont_form()
        #log = get_log()
	return render(request,"main.html",{'searchpoint':searchpoint,'discont':discont})


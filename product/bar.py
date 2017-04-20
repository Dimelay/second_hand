#!/usr/bin/python
# -*- coding: utf-8 -*-
from reportlab.graphics.barcode import code39, code128, code93
from reportlab.graphics.barcode import eanbc, qr, usps
from reportlab.graphics.shapes import Drawing
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics import renderPDF
from io import BytesIO

def createBarCodes(pr):
    """
    Create barcode examples and embed in a PDF
    """
    #c = canvas.Canvas("/tmp/barcodes.pdf", pagesize=letter)
    buff = BytesIO()
    c = canvas.Canvas(buff, pagesize=letter)
    pdfmetrics.registerFont(TTFont('FreeSans', 'FreeSans.ttf'))
    c.setFont("FreeSans",12)
    
    a=5
    b=-10
    cc=5
    y = 780
    d=0
    next_page=0
    for i in pr:
        barcode128 = code128.Code128(i.pid)
        c.drawString(cc,y,'ИП Мелай О.В')
        y = y - 7 * mm
        barcode128.drawOn(c,b,y)
        y = y - 5 * mm
        c.drawString(cc,y,i.pid)
        y = y - 5 * mm
        c.drawString(cc,y,'%s руб.' % str(i.price))
        y = y - 10 * mm
        d=d+1
        next_page=next_page+1
        if d == 10:
            y=780
            a=a+130
            b=b+130
            cc=cc+130
            d=0
        #if next_page == 36:
        if next_page == 50:
            c.showPage()
            c.setFont("FreeSans",12)
            a=5
            b=-10
            cc=5
            y = 780
            next_page=0

    c.save()
    pdf = buff.getvalue()
    buff.close()
    return pdf


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

from random import choice
from string import lowercase

def createBarCodes():
    """
    Create barcode examples and embed in a PDF
    """
    c = canvas.Canvas("barcodes.pdf", pagesize=letter)
    pdfmetrics.registerFont(TTFont('FreeSans', 'FreeSans.ttf'))
    c.setFont("FreeSans",12)
    barcode_value=["1475473366.0","1475481140.0","1475482368.0","1490611459.0"]
    """
    for i in range(0,140):
    """
        #barcode_value.append("".join(choice(lowercase) for i in range(10)))
    a=20
    b=5
    cc=20
    y = 750
    d=0
    next_page=0
    for i in barcode_value:
        barcode128 = code128.Code128(i)
        c.drawString(a,y,'ИП Мелай О.В')
        y = y - 10 * mm
        barcode128.drawOn(c,b,y)
        y = y - 5 * mm
        c.drawString(cc,y,i)
        y = y - 5 * mm
        c.drawString(cc,y,'300 руб')
        y = y - 10 * mm
        d=d+1
        next_page=next_page+1
        if d == 9:
            y=750
            a=a+130
            b=b+130
            cc=cc+130
            d=0
        if next_page == 36:
            c.showPage()
            c.setFont("FreeSans",12)
            a=20
            b=5
            cc=20
            y = 750
            next_page=0




    '''
for i in range(0,4):
            print a
        for i in range(0,8):
            c.drawString(a,y,'ИП Мелай О.В')
            y = y - 10 * mm
            barcode128.drawOn(c,b,y)
            y = y - 5 * mm
            c.drawString(cc,y,barcode_value)
            y = y - 5 * mm
            c.drawString(cc,y,'300 руб')
            y = y - 10 * mm
        a=a+130
        b=b+130
        cc=cc+130
    '''
#    for code in codes:
 #       code.drawOn(c, x, y)
    '''
    # draw the eanbc8 code
    barcode_eanbc8 = eanbc.Ean8BarcodeWidget(barcode_value)
    bounds = barcode_eanbc8.getBounds()
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    d = Drawing(50, 10)
    d.add(barcode_eanbc8)
    renderPDF.draw(d, c, 15, 555)

    # draw the eanbc13 code
    barcode_eanbc13 = eanbc.Ean13BarcodeWidget(barcode_value)
    bounds = barcode_eanbc13.getBounds()
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    d = Drawing(50, 10)
    d.add(barcode_eanbc13)
    renderPDF.draw(d, c, 15, 465)

    # draw a QR code
    qr_code = qr.QrCodeWidget('www.mousevspython.com')
    bounds = qr_code.getBounds()
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    d = Drawing(45, 45, transform=[45./width,0,0,45./height,0,0])
    d.add(qr_code)
    renderPDF.draw(d, c, 15, 405)
    '''
    c.save()

if __name__ == "__main__":
    createBarCodes()

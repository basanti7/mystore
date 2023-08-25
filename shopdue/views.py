from django.http import HttpResponse
import json
from django.shortcuts import render
from django.shortcuts import redirect
from shopdue import models
# Create your views here.


def detailOfSingleBill(request, invoice_no):
    query = request.GET.get('query')
    print("query string is " + str(query))
    purchase_list = models.Purchase.objects.filter(bill='26349aaa-8dd2-4e84-a554-f141a4218e0c')
    for itt in purchase_list:
        print('item - ' + itt.item + " .... Price - " + str(itt.price) + '-- total == ' + str(itt.total))

    return HttpResponse("Detailed bill returned successfully invoice --- " + str(invoice_no) )

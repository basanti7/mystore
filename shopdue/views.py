from django.http import HttpResponse
import json
from django.shortcuts import render
from django.shortcuts import redirect
from shopdue import models
from django.db.models import Sum
# Create your views here.


def detailOfSingleBill(request, invoice_no):
    query = request.GET.get('query')
    print("query string is " + str(query))
    purchase_list = models.Purchase.objects.filter(
        bill='26349aaa-8dd2-4e84-a554-f141a4218e0c')
    for itt in purchase_list:
        print('item - ' + itt.item + " .... Price - " +
              str(itt.price) + '-- total == ' + str(itt.total))
    return HttpResponse("Detailed bill returned successfully invoice --- " + str(invoice_no))


def showPaymentPage(request):
    data = {
        'page_title': 'Payment'
    }
    profile_id = request.GET.get('id')
    customer = None
    try:
        customer = models.Customer.objects.get(id=profile_id)
        # Replace 'YourModel' with the name of your model
        # 'id' is the field you want to use for the lookup, replace it if necessary
    except models.Customer.DoesNotExist:
        # Handle the case where the object with the specified 'id' does not exist
        customer = None
    print(customer)
    customer.total_due = models.Bill.objects.filter(customer=customer).aggregate(tot_due = Sum('due'))['tot_due']
    print(customer.total_due)
    # cust.total_due = models.Bill.objects.filter(customer=cust).aggregate(tot_due = Sum('due'))['tot_due']
    #     if cust.total_due is not None:
    #         shop_due_total += cust.total_due
    data['total_due'] = customer.total_due

    print('profile id is : ' + str(profile_id))
    return render(request, 'payment.html', data)

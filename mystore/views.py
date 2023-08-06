from django.http import HttpResponse
import json
from django.shortcuts import render
from shopdue import models


def homePage(request):
    data = {
        'page_title': 'Home'
    }
    magic_customers = models.Customer.objects.all()
    data['customers'] = magic_customers
    # customer_list = []
    # for customer in magic_customers:
    #     print(customer.customer_name)

    return render(request, 'index.html', data)


def customerRegistration(request):
    data = {
        'page_title': 'New Customer'
    }
    if request.method == 'POST':
        # Use request.POST dictionary to access the form data
        customer_name = request.POST.get('customer_name')
        customer_address = request.POST.get('customer_address')
        contact_number = request.POST.get('contact_number')
        additional_info = request.POST.get('additional_info')
        customer_image = request.FILES.get('customer_image')

        # Create a new instance of the model and save the image
        instance = models.Customer(customer_name=customer_name, customer_address=customer_address,
                                   contact_number=contact_number, additional_info=additional_info)
        instance.customer_image = customer_image
        instance.save()
        # You can now process the data as per your requirements
        # For example, you can save it to the database or perform some action with it
        # For now, let's just return a response to show the captured data
        return render(request, 'customer_registration.html', data)
    else:
        return render(request, 'customer_registration.html', data)


def customerProfile(request, customer_id):
    customer = models.Customer.objects.get(pk=customer_id)
    data = {'customer': customer}
    return render(request, 'customer_profile.html', data)


def invoiceOfSingleCustomer(request):
    json_string = '[{"serial":1,"product":"wer","price":33,"quantity":4,"total":132},{"serial":1,"product":"fsd","price":3,"quantity":4,"total":12}]'
    python_arr = json.loads(json_string)

    for obb in python_arr:
        print(obb['product'] + 'sal')

    if request.method == 'POST':
        # Use request.POST dictionary to access the form data
        products = request.POST.get('products')
        dis = request.POST.get('discount')
        temp_arr = json.loads(products)
        discount = 0

        if dis != None:
            discount = int(dis)
        total = 0
        paid = 0
        due = 0

        for obb in temp_arr:
            total += obb['total']

        total -= discount
        print("total is " + str(total))
        # generate a new bill with new invoice number
        # customer = foreign key of customer
        bill_instnce = models.Bill(
            customer_id=21, discount=4, total=total, paid=0, due=total)
        bill_instnce.save()
        print('Saving')

        for product in temp_arr:
            instance = models.Purchase(
                bill=bill_instnce, item=product['item'], price=product['price'], quantity=product['quantity'])
            instance.save()
    return render(request, 'invoice.html')

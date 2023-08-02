from django.http import HttpResponse
from django.shortcuts import render
from shopdue import models


def homePage(request):
    data = {
        'page_title': 'Home'
    }
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

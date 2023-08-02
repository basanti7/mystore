from django.contrib import admin
from shopdue.models import Customer
from shopdue.models import Bill
from shopdue.models import Purchase
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_address',
                    'contact_number', 'additional_info', 'customer_image' )


class BillAdmin(admin.ModelAdmin):
    list_display = ['customer', 'invoice_no',
                    'discount', 'total', 'paid', 'due']


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['bill', 'item', 'price', 'quantity']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Bill, BillAdmin)
admin.site.register(Purchase, PurchaseAdmin)
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from shopdue import views

urlpatterns = [
    path('bill/details/<str:invoice_no>', views.detailOfSingleBill, name='single_bill_detail'),
    path('bill/payment', views.showPaymentPage, name='show_payment_page')
]
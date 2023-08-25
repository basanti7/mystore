from django.http import HttpResponse
import json
from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.

def detailOfSingleBill(request):
    return HttpResponse("Detailed bill returned successfully")

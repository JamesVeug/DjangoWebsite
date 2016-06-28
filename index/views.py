from django.http import  HttpResponse, Http404
from django.shortcuts import render
from .models import  Customer


def index(request):
    all_customers = Customer.objects.all()
    context = {
        'all_customers' : all_customers,
    }

    return render(request, "index/index.html", context)

def detail(request, customer_id):
    try:
        customer = Customer.objects.get(pk=customer_id)
    except Customer.DoesNotExist:
        raise Http404("Customer does not exist")

        return render(request, "index/detail.html", context)
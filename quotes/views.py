from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Stock
from .forms import StockForm


# Create your views here.

def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        # pk_6d69e7c204024d179f9b2e76dac0a95f
        api_request = requests.get(
            "https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_6d69e7c204024d179f9b2e76dac0a95f")
        try:
            api = json.loads(api_request.content)

        except Exception as e:
            api = "Error..."

        return render(request, 'home.html', {'api': api})

    else:
        return render(request, 'home.html', {'ticker': "Enter a ticker symbol above..."})

    return render(request, 'home.html', {'api': api})


def about(requst):
    return render(requst, 'about.html', {})


def add_stock(request):

    if request.method == 'POST':
        form = StockForm(request.POST or None)
        form.save()
        messages.success(request, ("Stock has been added"))
        return redirect('add_stock')

    else:
        ticker = Stock.objects.all()
        return render(request, 'add_stock.html', {'ticker': ticker})

def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("Stock has been deleted"))
    return redirect(add_stock)


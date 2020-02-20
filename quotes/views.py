from django.shortcuts import render

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




    return render(request,'home.html', {'api': api})

def about(requst):
    return  render(requst,'about.html',{})
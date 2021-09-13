from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
# Create your views here.

def Index(request):
    return render(request, 'index.html')

def GetData(request):
    url = 'https://drive.google.com/uc?id=1tQRD6Qt-cvcdoOCNC--aOI16IOnVCYfb1Be4-cwOUf4'
    df = pd.read_csv(url)
    data = df.to_csv()
    return HttpResponse(data)

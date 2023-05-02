from django.shortcuts import render

# Create your views here.

def Usd_filters(request):
    d={'data':'Hello..I am CHanDaNa','me':'Hii....I am chandana kamalapuram'}
    return render(request,'Usd_filters.html',d)
from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    all_phone = Phone.objects.all()
    param = request.GET.get('sort', '')
    if param == 'name':
        phones = all_phone.order_by('name')
    elif param == 'min_price':
        phones = all_phone.order_by('price')
    elif param == 'max_price':
        phones = all_phone.order_by('-price')
    else:
        phones = all_phone
    context = {'phones': phones}
    return render(request, template, context)

def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)

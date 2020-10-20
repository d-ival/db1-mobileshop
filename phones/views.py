from django.shortcuts import render, redirect, reverse
from phones.models import Phone

def show_main(request):
    return redirect(reverse('phones_catalog'))


def show_catalog(request):
    order_type = request.GET.get('sort', 'name')
    template = 'catalog.html'

    if order_type == 'min_price':
        ordered_phones = Phone.objects.all().order_by('price')
    elif order_type == 'max_price':
        ordered_phones = Phone.objects.all().order_by('-price')
    else:
        ordered_phones = Phone.objects.all().order_by('name')

    context = {
        'ordered_phones':ordered_phones,
        'phones_catalog_url': reverse('phones_catalog')
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug__exact=slug)
    context = {
        'phone': phone,
        'phones_catalog_url': reverse('phones_catalog')
    }
    return render(request, template, context)

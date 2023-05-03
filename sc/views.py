import json

from django.shortcuts import render, HttpResponse
from .models import Services, SubCategory, AtomCategory, Order
from django.db.models.functions import Replace
from django.db.models import F, Value, CharField, IntegerField, ExpressionWrapper
from django.conf.urls.static import static
# from django.contrib.auth


# Create your views here.


def home(request):
    services = Services.objects.all().order_by('uid')
    return render(request, 'index.html', {'data': services})


def services(request, service, uid):
    services = Services.objects.all()
    active = services.filter(uid=uid).first()
    services = services.exclude(uid=uid)
    sub = SubCategory.objects.filter(service__uid=uid)
    return render(request, 'cat.html', {'services': services, 'active': active, 'sub': sub})


def select(request, service, service_uid, sub_name, sub_uid):

    services = Services.objects.all()
    active = services.filter(uid=service_uid).first()
    services = services.exclude(uid=service_uid)

    sub = SubCategory.objects.filter(service__uid=service_uid)
    active_sub = sub.filter(uid=sub_uid).first()
    sub = sub.exclude(uid=sub_uid)

    products = AtomCategory.objects.filter(atom__uid=sub_uid)
    return render(request, 'sub-cat.html', {'services': services, 'active': active, 'sub': sub,
                                            'active_sub': active_sub, 'prods': products})


def checkout(request):
    try:
        data = request.POST.get('form_cart')
        print(data)
        data = json.loads(data)

        prods = []
        for i in data:
            print(data[i]['qty'])
            prods += AtomCategory.objects.filter(uid=i).annotate(qty=Value(data[i]['qty'], output_field=IntegerField()),
                                                                 total = ExpressionWrapper((data[i]['qty'] * F('price')), output_field=IntegerField()))
        print(prods)

        return render(request, 'checkout.html', {'data': prods})
    except:

        return render(request, 'checkout.html')


def my_orders(request):
    try:
        if request.session['auth']:
            if request.session['auth'] == True:
                return HttpResponse(json.dumps(True))
    except:
        return HttpResponse(json.dumps(False))


def send_otp(request):

    email = request.POST.get('email')
    request.session['email'] = email
    request.session['auth'] = True

    return HttpResponse(json.dumps(True))


def success(request):

    try:

        data = json.loads(request.POST.get('form_cart'))
        data = json.dumps(data)
        email = request.session['email']
        print(data)

        Order(email = email, order=data).save()

        return render(request, 'success.html', {'data': data})

    except:
        return HttpResponse('Invalid Request')


def login(request):

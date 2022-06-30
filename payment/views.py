from django.shortcuts import render

# Create your views here.


def starter(request):
    return render(request, 'payment/starter.html')


def compact(request):
    return render(request, 'payment/compact.html')


def compact_plus(request):
    return render(request, 'payment/compact_plus.html')


def premium(request):
    return render(request, 'payment/premium.html')

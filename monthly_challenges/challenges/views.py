from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
# Create your views here.


def monthly_challenge(request, month):
    response = ''
    if month == 'january':
        response = 'Jan : 100 puhsup!'
    elif month == 'february':
        response = 'Feb : 200 skips!'
    else :
        return HttpResponseNotFound('Month entered is not available !')
    return HttpResponse(response)

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenge_dict = {
    'january':'Jan: 100 pushups!',
    'february':'Feb: 100 pushups!',
    'march':'Mar: 100 pushups!',
    'april':'Apr: 100 pushups!',
    'may':'May: 100 pushups!',
    'june':'Jun: 100 pushups!',
    'july':'July: 100 pushups!',
    'august':'Aug: 100 pushups!',
    'september':'Sept: 100 pushups!',
    'october':'Oct: 100 pushups!',
    'november':'Nov: 100 pushups!',
    'december':'Dec: 100 pushups!',

}

def monthly_challenge_by_number(request,month):
    months = list(monthly_challenge_dict.keys())
    if month==0 or month > len(months):
        return HttpResponseNotFound('Invalid month')
    redirect_link = months[month-1]
    redirect_path = reverse('month-challenge', args = [redirect_link])   #/challenge/january is created here 
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        response = monthly_challenge_dict[month] 
        return render(request, 'challenges/challenge.html')
    except:
        return HttpResponseNotFound('Month entered is not available !')


def index(request):
    list_code = ''
    months = monthly_challenge_dict.keys()
    for m in months:
        month_path = reverse('month-challenge',args = [m])
        list_code += f'<li><a href = \"{month_path}\">{m.upper()}</li>'
    return HttpResponse(list_code)

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request,'blog/homepage.html')
    # return HttpResponse('Hello! Welcome to the homepage.')


def posts(request):
    return HttpResponse('This is the all posts page')


def post(request,slug):
    return HttpResponse('This is individual post page ' + slug)
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'orders/index.html')

def my_profile(request):
    return render(request, 'accounts/index.html')
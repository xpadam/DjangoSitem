from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse('anasayfa')

def hakkimizda(request):
    return HttpResponse('Hakkimizda Sayfasi')

def iletisim(request):
    return HttpResponse('İletişim Sayfasi')
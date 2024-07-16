
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

# Create your views here.

data = {
    "programlama":"Programlama Kategorisine ait Kurslar",
    "web-gelistirme":"web gelistirme Kategorisine ait Kurslar",
    "mobil":"mobil Kategorisine ait Kurslar",
}


def kurslar(request):
    return HttpResponse('Kurs Listesi')

def programlama(request, kurs_adi):
    return HttpResponse('Programlama Listesi')

def mobiluygulamalar(request):
    return HttpResponse('Mobil Uygulamalar Kurs Listesi')

def details(request):
    return HttpResponse(f"{kurs_adi} Kurs Detay Sayfası")

def getCoursesByCategoryId(request, category_name):
    category_text = data[category_name];
    return HttpResponse(category_text)

def getCoursesByCategoryId(request, category_id):
    return redirect('/kurs/kategori/programlama')
from django.urls import path
from.import views


# http://127.0.0.1:8000/  => anasayfa
# http://127.0.0.1:8000/home  => anasayfa
# http://127.0.0.1:8000/kurslar  => Kurs Listesi


urlpatterns = [
    path('', views.kurslar),
    path('list', views.kurslar),
    path('details', views.details),
    path('programlama', views.programlama),
    path('mobil-uygulamalar', views.mobiluygulamalar),
    path('kategori/<int:category_id>', views.getCoursesByCategoryId),
    path('kategori/<str:category_name>', views.getCoursesByCategory),
]

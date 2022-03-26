from unicodedata import name
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns=[
    path('',views.show,name='home'),
    path('reg/',views.register,name='register'),
    path('exist/',views.existing,name='existing'),
    path('search/',views.search,name='search'),
     path('drop/',views.dropout,name='drop'),


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
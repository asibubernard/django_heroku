from django.contrib import admin
from django.urls import path, include # new
from .views import country

urlpatterns = [
    path('nothing-admin/', admin.site.urls), # new
    path('country/', country, name="country"),
    path('', include('pages.urls')), # new
]

from django.contrib import admin
from django.urls import path
from event import views  # Import views from the 'event' app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),  # Redirect root URL to the home page
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('inventory/', views.inventory, name='inventory'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
]

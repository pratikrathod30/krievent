from django.urls import path
from .views import contact, home, about, services, inventory, gallery

urlpatterns = [
    path("", home, name="home"),
    path("contact/", contact, name="contact"),
    path("about/", about, name="about"),
    path("services/", services, name="services"),
    path("inventory/", inventory, name="inventory"),
    path("gallery/", gallery, name="gallery"),
]

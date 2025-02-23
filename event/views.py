from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')  # Ensure 'contact' URL is set correctly
    else:
        form = ContactForm()

    return render(request, "event/contact.html", {"form": form})


def home(request):
    return render(request, "event/home.html")

def about(request):
    return render(request, "event/about.html")

def services(request):
    return render(request, "event/services.html")

def inventory(request):
    return render(request, "event/inventory.html")

def gallery(request):
    return render(request, "event/gallery.html")

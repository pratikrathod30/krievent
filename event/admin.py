from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'event_type', 'created_at')
    search_fields = ('name', 'email', 'event_type')

admin.site.register(Contact, ContactAdmin)

# django level imports
from django.contrib import admin

# project level imports
from .models import Publisher


class PublisherAdmin(admin.ModelAdmin):
    """
    This class handles Admin panel for Publisher class
    """
    list_display = ['id', 'name']
    list_display_links = ['id']
    search_fields = ['name']
    readonly_fields = ['slug']

    class Meta:
        model = Publisher


admin.site.register(Publisher, PublisherAdmin)

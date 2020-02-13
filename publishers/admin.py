from django.contrib import admin

# project level imports
from .models import Publisher


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id']
    search_fields = ['name']

    class Meta:
        model = Publisher


admin.site.register(Publisher, PublisherAdmin)

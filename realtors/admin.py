from django.contrib import admin
from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'is_mvp')
    list_per_page = 10
    search_fields = ('id', 'name')
    list_display_links = ('id', 'name')


admin.site.register(Realtor, RealtorAdmin)

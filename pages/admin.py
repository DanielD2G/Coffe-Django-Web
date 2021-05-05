from django.contrib import admin
from .models import Page
# Register your models here.
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('date_creation', 'date_modified')
    list_display = ('title', 'order')

admin.site.register(Page, PageAdmin)
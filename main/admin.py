from django.contrib import admin
from .models import Language, Bedroom
# Register your models here.


class LanguageAdmin(admin.ModelAdmin):
    ''' Language data on admin page '''
    list_display = ('id', 'name')
    list_display_links = ('name',)


class BedroomAdmin(admin.ModelAdmin):
    ''' Bedroom data on admin page '''
    list_display = ('id', 'language', 'description', 'keywords')
    list_display_links = ('id',)
    search_fields = ('description', 'keywords')


admin.site.register(Language, LanguageAdmin)
admin.site.register(Bedroom, BedroomAdmin)
from django.contrib import admin
from .models import Language, Bedroom, Profile
# Register your models here.


class LanguageAdmin(admin.ModelAdmin):
    ''' Language data on admin page '''
    list_display = ('id', 'name')
    list_display_links = ('name',)


class BedroomAdmin(admin.ModelAdmin):
    ''' Bedroom data on admin page '''
    list_display = ('id', 'language', 'keywords', 'description')
    list_display_links = ('id',)
    search_fields = ('description', 'keywords')


class ProfileAdmin(admin.ModelAdmin):
    ''' Profile data on admin page '''
    list_display = ('id', 'user', 'language')
    list_display_links = ('user',)


admin.site.register(Language, LanguageAdmin)
admin.site.register(Bedroom, BedroomAdmin)
admin.site.register(Profile, ProfileAdmin)
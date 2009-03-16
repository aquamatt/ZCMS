from django.contrib import admin
from zcms.models import *

class CMSComponentAdmin(admin.ModelAdmin):
    list_display = ('id', 'cid', 'channel', 'language', 'shortValue')
    list_filter = ('channel', 'language')
    search_fields = ('cid', 'value')
admin.site.register(CMSComponent, CMSComponentAdmin)

class CMSTokenAdmin(admin.ModelAdmin):
    list_display = ('id', 'cid', 'channel', 'language', 'value')
    list_filter = ('channel', 'language')
    search_fields = ('cid', 'value')
admin.site.register(CMSToken, CMSTokenAdmin)

class URLAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'component_name', 'enabled')
    search_fields = ('name', 'url')
    list_filter = ('enabled', )
admin.site.register(URL, URLAdmin)

class ChannelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent')
admin.site.register(Channel, ChannelAdmin)

class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'iso_code', 'name')

admin.site.register(Language, LanguageAdmin)

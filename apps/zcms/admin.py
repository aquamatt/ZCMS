from django.contrib import admin
from zcms.models import *

class CMSComponentAdmin(admin.ModelAdmin):
    list_display = ('cid', 'channel', 'shortValue')
    list_filter = ('channel', )
    search_fields = ('cid', 'value')
    ordering = ('cid','channel')
admin.site.register(CMSComponent, CMSComponentAdmin)

class CMSTokenAdmin(admin.ModelAdmin):
    list_display = ('cid', 'language', 'value')
    list_filter = ('language', )
    search_fields = ('cid', 'value')
    ordering = ('cid','language')
admin.site.register(CMSToken, CMSTokenAdmin)

class URLAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'component_name', 'enabled')
    search_fields = ('name', 'url')
    list_filter = ('enabled', )
admin.site.register(URL, URLAdmin)

class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    ordering = ('name',)
admin.site.register(Channel, ChannelAdmin)

class LanguageAdmin(admin.ModelAdmin):
    list_display = ('iso_code', 'name', 'fallback')
    ordering = ('iso_code',)
admin.site.register(Language, LanguageAdmin)

class SlotContentInline(admin.TabularInline):
    model = SlotContent

class SlotAdmin(admin.ModelAdmin):
    list_display = ('slot', 'summary')
    inlines = [SlotContentInline,]
admin.site.register(Slot, SlotAdmin)

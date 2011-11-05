from django.contrib import admin
from zcms.models import *

class ComponentInline(admin.TabularInline):
    model = CMSComponentValue
    extra = 1
    
class CMSComponentAdmin(admin.ModelAdmin):
    inlines = [ComponentInline,]
admin.site.register(CMSComponent, CMSComponentAdmin)

class TokenInline(admin.TabularInline):
    model = CMSTokenValue
    extra = 1

class CMSTokenAdmin(admin.ModelAdmin):
    inlines = [TokenInline,]
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
    extra = 1

class SlotAdmin(admin.ModelAdmin):
    list_display = ('slot', 'summary')
    inlines = [SlotContentInline,]
    extra = 1
admin.site.register(Slot, SlotAdmin)

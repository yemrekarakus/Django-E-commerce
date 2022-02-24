from django.contrib import admin
from .models import Page, Carousel



class PageAdmin(admin.ModelAdmin):
     list_display = ('pk','title','slug','status','updated_at')
     list_filter = ('status',)
     list_editable = ('title','status')


admin.site.register(Page,PageAdmin)

admin.site.register(Carousel)

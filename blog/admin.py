from django.contrib import admin
from blog.models import blogs

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('css/main.css',)
        }
        js = ('js/blog.js', )


admin.site.register(blogs,BlogAdmin)

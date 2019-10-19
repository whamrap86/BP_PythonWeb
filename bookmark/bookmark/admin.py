from django.contrib import admin

# Register your models here.
from .models import Bookmark

class BookmarkAdmin(admin.ModelAdmin):
    model = Bookmark
    list_display = ('site_name', 'url')

admin.site.register(Bookmark)
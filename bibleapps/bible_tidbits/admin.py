from django.contrib import admin
from bibleapps.bible_tidbits.models import Tidbit, Tag

class TagAdmin(admin.ModelAdmin):
	search_fields = ['tag', 'category']

admin.site.register(Tidbit)
admin.site.register(Tag, TagAdmin)
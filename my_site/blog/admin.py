from django.contrib import admin
from .models import post,Author,Tag


class PostAdmin(admin.ModelAdmin):
    list_filter=("author","tags","date",) #to filter in the admin page by
    list_display=("title","date","author",)
    prepopulated_fields={"slug":("title",)} #for auto fill field

admin.site.register(post,PostAdmin) # we pass the class and the admin func to sort
admin.site.register(Author)
admin.site.register(Tag)

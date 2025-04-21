from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import comment

# Register your models here.
from .models import Category,Ebook,audiobook
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =['c_name','description']

@admin.register(Ebook)
class EbookAdmin(admin.ModelAdmin):
    list_display =['name','simage','price','detail','category','author','pdf','uploaded']

    def simage(self,oj):
        if oj.image:
            return mark_safe(f'<img src="{oj.image.url}"width="50" height="50">')
        return "no image"

@admin.register(comment) 
class usercomment(admin.ModelAdmin):  
    list_display = ['name','email', 'message','uploaded']

@admin.register(audiobook)
class AudiobookAdmin(admin.ModelAdmin):
    list_display =['name','simage','price','detail','category','author','audio','uploaded']

    def simage(self,oj):
        if oj.image:
            return mark_safe(f'<img src="{oj.image.url}"width="50" height="50">')
        return "no image"
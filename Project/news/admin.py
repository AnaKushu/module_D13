from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'dateCreation')
    list_filter = ('title', 'postCategory', 'dateCreation')
    search_fields = ('title', 'postCategory__name')


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Comment)
admin.site.register(Subscriber)

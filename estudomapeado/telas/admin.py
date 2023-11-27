from django.contrib import admin
from .models import Category, Comment, Texto, Video


class CategoryAdmin(admin.ModelAdmin):
    pass


class TextoAdmin(admin.ModelAdmin):
    pass

class VideoAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Texto, TextoAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Comment, CommentAdmin)
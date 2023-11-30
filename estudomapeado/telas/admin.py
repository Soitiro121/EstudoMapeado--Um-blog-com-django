from django.contrib import admin
from .models import CategoryTexto,CategoryVideo, ForumMessage, Texto, Video


class CategoryTextoAdmin(admin.ModelAdmin):
    pass


class CategoryVideoAdmin(admin.ModelAdmin):
    pass


class TextoAdmin(admin.ModelAdmin):
    pass


class VideoAdmin(admin.ModelAdmin):
    pass


class ForumMessageAdmin(admin.ModelAdmin):
    pass


admin.site.register(CategoryTexto, CategoryTextoAdmin)
admin.site.register(CategoryVideo, CategoryVideoAdmin)
admin.site.register(Texto, TextoAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(ForumMessage, ForumMessageAdmin)
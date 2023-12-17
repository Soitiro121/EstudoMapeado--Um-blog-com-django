from django.contrib import admin
from .models import CategoryTexto, CategoryVideo, ForumMessage, Texto, Video, Comentario


class CategoryTextoAdmin(admin.ModelAdmin):
    pass


class CategoryVideoAdmin(admin.ModelAdmin):
    pass


class TextoAdmin(admin.ModelAdmin):
    pass


class VideoAdmin(admin.ModelAdmin):
    pass


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('texto', 'autor', 'data_criacao', 'conteudo')
    list_filter = ('data_criacao', 'autor')
    search_fields = ('conteudo', 'autor__username', 'texto__title')


class ForumMessageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(CategoryTexto, CategoryTextoAdmin)
admin.site.register(CategoryVideo, CategoryVideoAdmin)
admin.site.register(Texto, TextoAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(ForumMessage, ForumMessageAdmin)
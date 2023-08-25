from django.contrib import admin

from board.models import Board, Column, Task


class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    filter_horizontal = ('column', 'users')

admin.site.register(Board, BoardAdmin)


class ColumnAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    filter_horizontal = ('card',)

admin.site.register(Column, ColumnAdmin)


class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    search_fields = ('title',)

admin.site.register(Task, CardAdmin)

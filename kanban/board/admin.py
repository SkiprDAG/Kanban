from django.contrib import admin

from board.models import Board, Column, Card


class BoardAdmin(admin.ModelAdmin):
    list_display = ('codename', 'name',)
    list_display_links = ('codename', 'name',)
    search_fields = ('name',)
    filter_horizontal = ('column',)

admin.site.register(Board, BoardAdmin)


class ColumnAdmin(admin.ModelAdmin):
    list_display = ('codename', 'name',)
    list_display_links = ('codename', 'name',)
    search_fields = ('name',)
    filter_horizontal = ('card',)

admin.site.register(Column, ColumnAdmin)


class CardAdmin(admin.ModelAdmin):
    list_display = ('codename', 'name',)
    list_display_links = ('codename', 'name',)
    search_fields = ('name',)

admin.site.register(Card, CardAdmin)

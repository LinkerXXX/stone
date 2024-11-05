from django.contrib import admin
from board.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    listdisplay = ("text", "name", "user")
    ordering = ["creation_date", "user"]

from django.views.generic import ListView
from board.models import Note


class NoteListView(ListView):
    model = Note
    template_name = "board/base.html"
    context_object_name = "notes"  # Имя переменной, доступной в шаблоне

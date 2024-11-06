from django.views.generic import ListView
from board.models import Note
from django.views.generic.edit import CreateView, UpdateView
from board.forms import NoteCreateForm
from user.models import User
from django.shortcuts import redirect


class NoteListView(ListView):
    model = Note
    template_name = "board/base.html"
    context_object_name = "notes"


class NoteCreateView(CreateView):
    model = Note
    template_name = "board/note_create.html"
    form_class = NoteCreateForm

    def form_valid(self, form):
        form.instance.user = User.objects.get(username=self.request.user.username)
        user = form.save()
        return redirect("board_note_list")

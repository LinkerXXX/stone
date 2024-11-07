from django.views.generic import ListView
from board.models import Note
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from board.forms import NoteCreateForm
from user.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy


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


class NoteUpdateView(UpdateView):
    model = Note
    queryset = Note.objects.all()
    fields = ["name", "text"]
    success_url = "/user/{id}"
    template_name = "board/note_update.html"

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return redirect("user_detail", self.object.user.pk)


class NoteDeleteView(DeleteView):
    model = Note
    template_name = "board/note_delete.html"
    success_url = "/user/{id}"

    def get_success_url(self):
        user_id = self.request.user.id
        return reverse_lazy("user_detail", kwargs={"pk": user_id})

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["notes"] = Note.objects.all()
        return context

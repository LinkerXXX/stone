from board.models import Note
from django.forms import ModelForm


class NoteCreateForm(ModelForm):
    class Meta:
        model = Note
        fields = ["name", "text"]

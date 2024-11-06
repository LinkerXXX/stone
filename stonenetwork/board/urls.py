from django.urls import path
from board.views import NoteListView, NoteCreateView

urlpatterns = [
    path("news/", NoteListView.as_view(), name="board_note_list"),
    path("create/", NoteCreateView.as_view(), name="board_note_create"),
]

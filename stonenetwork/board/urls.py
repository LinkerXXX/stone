from django.urls import path
from board.views import NoteListView

urlpatterns = [
    path("news/", NoteListView.as_view(), name="board_note_list"),
]

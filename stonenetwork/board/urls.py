from django.urls import path
from board.views import NoteCreateView, NoteUpdateView, NoteDeleteView

urlpatterns = [
    path("create/", NoteCreateView.as_view(), name="board_note_create"),
    path("update/<int:pk>/", NoteUpdateView.as_view(), name="board_note_update"),
    path("delete/<int:pk>/", NoteDeleteView.as_view(), name="board_note_delete"),
]

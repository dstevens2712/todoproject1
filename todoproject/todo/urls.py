from django.urls import path
from todo.views import TodoDetailView, TodoListView
from todo.views import NoteDetailView, NoteListView

urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list'),
    path('<int:task_id>', TodoDetailView.as_view(), name='task'),
    path('', NoteDetailView.as_view(), name='note_list'),
    path('<int:task_id>', NoteListView.as_view(), name='note'),
]

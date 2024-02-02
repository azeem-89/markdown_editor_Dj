# markdown_editor_app/urls.py
from django.urls import path
from .views import markdown_editor

urlpatterns = [
    path('markdown_editor/', markdown_editor, name='markdown_editor'),
]

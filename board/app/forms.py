from django import forms
from .models import *


class MessagesForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            'nameCat',
            'title',
            'text',
            'files',
                   ]
        labels = {
            'nameCat': 'Категория',
            'title': 'Заголовок',
            'text': 'Текст',
            'files': 'Выберите файл',
                    }


class CommForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text',
        ]
        labels = {
            'text': 'Текст',
        }


class CommConfirmForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'status',
        ]
        labels = {
            'status': 'Принять комментарий?',
        }

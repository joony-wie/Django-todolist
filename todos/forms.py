# Django
from django import forms
# Project
from .models import Todo
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class TodoForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'text', 'deadline', 'priority', 'completed')
        # exclude = ['timestamp']
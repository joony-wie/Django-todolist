# Django
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
# Project
from .forms import TodoForm
from .models import Todo
from bootstrap_modal_forms.mixins import PassRequestMixin, DeleteAjaxMixin


class Index(generic.ListView):
    model = Todo
    context_object_name = 'todos'
    template_name = 'index.html'


# Create
class TodoCreateView(PassRequestMixin, SuccessMessageMixin,
                     generic.CreateView):
    template_name = 'todos/create_todo.html'
    form_class = TodoForm
    success_message = 'Success: Todo was created.'
    success_url = reverse_lazy('index')


# Update
class TodoUpdateView(PassRequestMixin, SuccessMessageMixin,
                     generic.UpdateView):
    model = Todo
    template_name = 'todos/update_todo.html'
    form_class = TodoForm
    success_message = 'Success: Todo was updated.'
    success_url = reverse_lazy('index')


# Read
class TodoReadView(generic.DetailView):
    model = Todo
    template_name = 'todos/read_todo.html'


# Delete
class TodoDeleteView(DeleteAjaxMixin, generic.DeleteView):
    model = Todo
    template_name = 'todos/delete_todo.html'
    success_message = 'Success: Todo was deleted.'
    success_url = reverse_lazy('index')
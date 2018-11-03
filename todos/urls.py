# Django
from django.urls import path
# Local
from todos import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('create/', views.TodoCreateView.as_view(), name='create_todo'),
    path('update/<int:pk>', views.TodoUpdateView.as_view(), name='update_todo'),
    path('read/<int:pk>', views.TodoReadView.as_view(), name='read_todo'),
    path('delete/<int:pk>', views.TodoDeleteView.as_view(), name='delete_todo'),
]
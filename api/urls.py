from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.BookCreateView.as_view(), name='book-list-create'),
    path('book/<int:pk>/', views.BookRetrieveUpdateDestroyView.as_view(), name='book-retrieve-update-destroy'),
]
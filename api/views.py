# Create your views here.

from rest_framework import generics

from .models import Book

from .serializers import BookSerializer


class BookCreateView(generics.ListCreateAPIView):

    queryset = Book.objects.all()

    serializer_class = BookSerializer


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Book.objects.all()

    serializer_class = BookSerializer 
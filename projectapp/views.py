from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer
from rest_framework import generics


class BookListApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class =BookSerializer
class BookDetailApiView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDeleteApiView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class BookUpdateApiView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateApiView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


#viewset
class BookViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



#function based view
# @api_view(['GET'])
# def book_list_view(request,*args,**kwargs):
#     books = Book.objects.all()
#     serializer = BookSerializer(books,many=True)
#     return Response(serializer.data)


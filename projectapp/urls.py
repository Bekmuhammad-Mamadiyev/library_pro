from django.urls import path
from .views import (BookListApiView,BookDetailApiView,BookDeleteApiView,BookUpdateApiView,
                    BookCreateApiView,BookListCreateView,BookUpdateDeleteView,BookViewset)
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('books',BookViewset,basename='books')


urlpatterns = [
    path('books/',BookListApiView.as_view()),
    path('booklistcreate/',BookListCreateView.as_view()),
    path('bookupdatedelete/<int:pk>/',BookUpdateDeleteView.as_view()),
    path('books/create/',BookCreateApiView.as_view()),
    path('books/<int:pk>/',BookDetailApiView.as_view()),
    path('books/<int:pk>/update/',BookUpdateApiView.as_view()),
    path('books/<int:pk>/delete/',BookDeleteApiView.as_view()),

]

urlpatterns =urlpatterns + router.urls
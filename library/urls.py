from django.urls import path
from django.views.generic import RedirectView  # Импортируем редирект
from . import views
from .views import (BooksListView, BookCreateView, BookDetailView, BookUpdateView,
                    BookDeleteView, AuthorCreateView, AuthorUpdateView, AuthorListView, RecommendBookView,
                    ReviewBookView)

app_name = 'library'

urlpatterns = [
    # Автоматический редирект с /library/ на /library/books/
    path('', RedirectView.as_view(pattern_name='library:books_list', permanent=False)),

    path('authors/', AuthorListView.as_view(), name='authors_list'),
    path('author/new/', AuthorCreateView.as_view(), name='author_create'),
    path('author/update/<int:pk>/', AuthorUpdateView.as_view(), name='author_update'),
    path('books/', BooksListView.as_view(), name='books_list'),
    path('books/new/', BookCreateView.as_view(), name='books_create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),
    path('books/recommend/<int:pk>/', RecommendBookView.as_view(), name='recommend_book'),
    path('books/review/<int:pk>/', ReviewBookView.as_view(), name='review_book'),
]

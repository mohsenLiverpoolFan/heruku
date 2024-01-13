from django.urls import path
from .views import AuthorView, BookView, BookDetailView, AuthorDetailView

app_name = 'bookreview'
urlpatterns = [
    path('authors/', AuthorView.as_view(), name='authors'),
    path('author/<int:pk>', AuthorDetailView.as_view(), name='author-detail'),
    path('books/', BookView.as_view(), name='book_view'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book_detail'),
]

from django.urls import path

from product.views import BookView, OneBookView, GenreView, OneGenreView, BookVS

app_name = 'product'

urlpatterns = [
    path('all', BookView.as_view(), name='books'),
    path('all2', BookVS.as_view({'get': 'list'}), name='books2'),
    path('genres', GenreView.as_view(), name='genres'),
    path('genres/<id>', OneGenreView.as_view(), name='genre'),
    path('<id>', OneBookView.as_view(), name='book'),

]

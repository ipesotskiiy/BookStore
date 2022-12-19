from django.urls import path

from product.views import BookView, OneBookView, GenreView

app_name = 'product'

urlpatterns = [
    path('all', BookView.as_view(), name='books'),
    path('genres', GenreView.as_view(), name='genres'),
    path('<id>', OneBookView.as_view(), name='book'),
    # path('rep/<id>', OneRepoView.as_view(), name='repo')
]

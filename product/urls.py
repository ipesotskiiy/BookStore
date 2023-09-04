from django.urls import path

from product.views import (
    BookView,
    OneBookView,
    GenreView,
    OneGenreView,
    CreateCommentView,
    CreateRatingView,
    RecommendationView,
    # AverRateView,
    FavoritesView
)

app_name = 'product'

urlpatterns = [
    path('all', BookView.as_view(), name='books'),
    path('add-comment', CreateCommentView.as_view(), name='add-comment'),
    path('rate', CreateRatingView.as_view(), name='add-rating'),
    path('recommendations&exclude=<id>', RecommendationView.as_view(), name='recommendations'),
    path('genres', GenreView.as_view(), name='genres'),
    path('genres/<id>', OneGenreView.as_view(), name='genre'),
    path('favorites', FavoritesView.as_view(), name='get_favorites'),
    path('favorites/<id>', FavoritesView.as_view(), name='delete_favorites'),
    path('add-favorites/<id>', FavoritesView.as_view(), name='add_favorites'),
    path('<id>', OneBookView.as_view(), name='book'),
]

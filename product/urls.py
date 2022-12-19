from django.urls import path

from product.views import BookView, OneBookView

app_name = 'product'

urlpatterns = [
    path('all', BookView.as_view(), name='books'),
    path('<id>', OneBookView.as_view(), name='book')
]

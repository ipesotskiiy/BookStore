from django.urls import path

from product.views import BookView

app_name = 'product'

urlpatterns = [
    path('all', BookView.as_view(), name='books')
]

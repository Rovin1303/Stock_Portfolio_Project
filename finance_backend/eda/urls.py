from django.urls import path
from .views import StockDetailAPIView

urlpatterns = [
    path('stock/<int:stock_id>/', StockDetailAPIView.as_view()),
]
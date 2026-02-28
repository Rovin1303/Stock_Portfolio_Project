from django.urls import path
from .views import (
    PortfolioView,
    PortfolioDetailView,
    StockView,
    StockDetailView
)

urlpatterns = [
    path('portfolio/', PortfolioView.as_view()),
    path('portfolio/<int:pk>/', PortfolioDetailView.as_view()),

    path('stocks/', StockView.as_view()),
    path('stocks/<int:pk>/', StockDetailView.as_view()),
]
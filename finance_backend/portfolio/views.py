from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Portfolio, Stock
from .serializers import PortfolioSerializer, StockSerializer


# ===============================
# PORTFOLIO LIST + CREATE
# ===============================
class PortfolioView(APIView):

    def get(self, request):
        portfolios = Portfolio.objects.all()
        serializer = PortfolioSerializer(portfolios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PortfolioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Portfolio created successfully"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ===============================
# PORTFOLIO DETAIL (GET, PUT, DELETE)
# ===============================
class PortfolioDetailView(APIView):

    def get_object(self, pk):
        try:
            return Portfolio.objects.get(pk=pk)
        except Portfolio.DoesNotExist:
            return None

    def get(self, request, pk):
        portfolio = self.get_object(pk)
        if not portfolio:
            return Response({"error": "Portfolio not found"}, status=404)

        serializer = PortfolioSerializer(portfolio)
        return Response(serializer.data)

    def put(self, request, pk):
        portfolio = self.get_object(pk)
        if not portfolio:
            return Response({"error": "Portfolio not found"}, status=404)

        serializer = PortfolioSerializer(portfolio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Portfolio updated successfully"})
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        portfolio = self.get_object(pk)
        if not portfolio:
            return Response({"error": "Portfolio not found"}, status=404)

        portfolio.delete()
        return Response({"message": "Portfolio deleted successfully"})


# ===============================
# STOCK LIST + CREATE
# ===============================
class StockView(APIView):

    def get(self, request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Stock added successfully"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ===============================
# STOCK DETAIL (GET, PUT, DELETE)
# ===============================
class StockDetailView(APIView):

    def get_object(self, pk):
        try:
            return Stock.objects.get(pk=pk)
        except Stock.DoesNotExist:
            return None

    def get(self, request, pk):
        stock = self.get_object(pk)
        if not stock:
            return Response({"error": "Stock not found"}, status=404)

        serializer = StockSerializer(stock)
        return Response(serializer.data)

    def put(self, request, pk):
        stock = self.get_object(pk)
        if not stock:
            return Response({"error": "Stock not found"}, status=404)

        serializer = StockSerializer(stock, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Stock updated successfully"})
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        stock = self.get_object(pk)
        if not stock:
            return Response({"error": "Stock not found"}, status=404)

        stock.delete()
        return Response({"message": "Stock deleted successfully"})
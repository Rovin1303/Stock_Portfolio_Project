from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services.stock_service import get_stock_analysis
from .serializers import StockAnalysisSerializer
from portfolio.models import Stock


class StockDetailAPIView(APIView):

    def get(self, request, stock_id):

        try:
            stock_obj = Stock.objects.get(id=stock_id)
        except Stock.DoesNotExist:
            return Response(
                {"error": "Stock not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        ticker = stock_obj.ticker

        data = get_stock_analysis(ticker)

        if not data:
            return Response(
                {"error": "Invalid ticker"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = StockAnalysisSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)
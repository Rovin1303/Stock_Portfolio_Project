from rest_framework import serializers
from .models import Portfolio, Stock

class StockSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField()

    class Meta:
        model = Stock
        fields = "__all__"

    def get_discount(self, obj):
        return obj.discount_level()


class PortfolioSerializer(serializers.ModelSerializer):
    stocks = StockSerializer(many=True, read_only=True)

    class Meta:
        model = Portfolio
        fields = "__all__"
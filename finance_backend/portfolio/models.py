from django.db import models
from staff.models import Staff


class Portfolio(models.Model):
    name = models.CharField(max_length=200)
    sector = models.CharField(max_length=200)
    created_by = models.ForeignKey(Staff, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Stock(models.Model):
    portfolio = models.ForeignKey(
        Portfolio,
        on_delete=models.CASCADE,
        related_name="stocks"
    )

    company_name = models.CharField(max_length=200)
    ticker = models.CharField(max_length=20, unique=True)

    current_price = models.FloatField()
    pe_ratio = models.FloatField()
    intrinsic_value = models.FloatField(null=True, blank=True)

    def discount_level(self):
        if self.intrinsic_value:
            return ((self.intrinsic_value - self.current_price) / self.intrinsic_value) * 100
        return 0

    def __str__(self):
        return self.company_name
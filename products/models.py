from django.core.validators import MinValueValidator
from django.db import models

class Product(models.Model):
    product_type = models.ForeignKey('product_types.ProductType',
                                     on_delete=models.CASCADE,
                                     verbose_name="Тип продукции")

    product_name = models.CharField(max_length=100,
                                    verbose_name="Наименование продукции")

    sku = models.PositiveIntegerField(verbose_name="Артикул")
    min_price = models.DecimalField(max_digits=10,
                                    decimal_places=2,
                                    validators=[MinValueValidator(0)],
                                    verbose_name="Минимальная стоимость для партнера"
                                    )

    def __str__(self):
        return self.product_name
from django.db import models

class ProductType(models.Model):
    product_type_name = models.CharField(max_length=100,
                                         verbose_name="Тип проудкции")
    coefficient = models.DecimalField(max_digits=5,
                                      decimal_places=2,
                                      verbose_name="Коэффициент типа продукции")

    def __str__(self):
        return self.product_type_name
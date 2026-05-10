from django.db import models


class PartnerProduct(models.Model):
    product = models.ForeignKey("products.Product",
                                on_delete=models.CASCADE,
                                verbose_name="Продукция", )
    partner = models.ForeignKey("partners.Partner",
                                on_delete=models.CASCADE,
                                verbose_name="Продукция",)
    amount = models.PositiveIntegerField(verbose_name="Количество продукции")

    sale_date = models.DateField(verbose_name="Дата продажи")

    def __str__(self):
        return str(self.product.pk)

    class Meta:
        ordering = ["sale_date"]
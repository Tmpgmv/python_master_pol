from django.db import models


class MaterialType(models.Model):
    material_type_name = models.CharField(max_length=100,
                                          verbose_name="Тип материала")

    deficiency_percentage = models.DecimalField(max_digits=5,
                                                decimal_places=2,
                                                verbose_name="Процент брака материала ")

    def __str__(self):
        return self.material_type_name
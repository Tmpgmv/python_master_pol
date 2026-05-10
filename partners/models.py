from django.db import models


class Partner(models.Model):
    CHOICES = (("ЗАО", "ЗАО"), ("ОАО", "ОАО"), ("ООО", "ООО"), ("ПАО", "ПАО"))
    type = models.CharField(max_length=50,
                            choices=CHOICES,
                            verbose_name="Тип партнера", )
    name = models.CharField(max_length=50, verbose_name="Наименование партнера")
    ceo = models.CharField(max_length=100, verbose_name="Директор")
    email = models.EmailField(max_length=100, verbose_name="Электронная почта")
    phone_number = models.PositiveBigIntegerField(verbose_name="Телефон")
    address = models.CharField(max_length=200, verbose_name="Юридический адрес")
    taxpayer_number = models.PositiveBigIntegerField(verbose_name="ИНН")
    rating = models.PositiveIntegerField(verbose_name="Рейтинг")

    def get_phone_number(self):
        formatted = "+{} {} {} {} {} {}".format(str(self.phone_number)[0],
                                                str(self.phone_number)[1:4],
                                                str(self.phone_number)[4:7],
                                                str(self.phone_number)[7:9],
                                                str(self.phone_number)[9:11],
                                                str(self.phone_number)[12:])
        return formatted

    def total_sale(self):
        total = 0

        for pp in self.partnerproduct_set.all():
            total += pp.amount

        return total

    def get_discount(self):
        discount = 0
        if (self.total_sale() >= 10000 and self.total_sale() < 50000):
            discount = 5
        elif (self.total_sale() >= 50000 and self.total_sale() < 300000):
            discount = 10
        elif (self.total_sale() >= 300000):
            discount = 15

        return f"{discount} %"

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

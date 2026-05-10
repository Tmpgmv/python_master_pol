import math

from general.exceptions import InvalidParamsException


class MaterialCalculator():
    def calculate_material(self,
                           product_type_id, # PKGH идентификатор типа продукции
                           mateirial_type_id, # PKGH идентификатор типа материала
                           produced_product_amount, # PKGH количество получаемой продукции
                           param_1, # PKGH параметр продукции
                           param_2): # PKGH параметр продукции

        """
        PKGH

        Метод для рассчита целого количества материала, необходимого
        для производства указанного количества продукции, учитывая возможный
        брак материала.
        """

        material_amount = 0 # количество необходимого материала с учетом возможного брака материала.


        try:
            self.validate_params(produced_product_amount,
                                 param_1,
                                 param_2)

        except (InvalidParamsException) as e:
            print(e)
            return -1


        material_amount = math.ceil(material_amount)
        assert material_amount >= 0, "Количество материала не может быть отрицательным" # PKGH Отладка.
        return material_amount

    def validate_params(self,
                        produced_product_amount,
                        param_1,
                        param_2):
        self.validate_produced_product_amount(produced_product_amount)
        self.validate_param(param_1, "param_1")
        self.validate_param(param_2, "param_2")

    def validate_produced_product_amount(self, produced_product_amount):
        if not isinstance(produced_product_amount, int):
            raise InvalidParamsException("produced_product_amount должено быть быть целым числом")

        if produced_product_amount <= 0:
            raise InvalidParamsException("produced_product_amount должено быть положительным числом")

    def validate_param(self, param, param_name):
        if not isinstance(param, (int, float)):
            raise InvalidParamsException(f"{param_name} должно быть вещественным числом")

        if param <= 0:
            raise InvalidParamsException(f"{param_name} должено быть положительным числом")
import math


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


        material_amount = math.ceil(material_amount)
        assert material_amount >= 0, "Количество материала не может быть отрицательным" # PKGH Отладка.
        return material_amount
from django.views.generic import TemplateView

from general.service import MaterialCalculator
from partner_products.models import PartnerProduct


class CalculateMaterialView(TemplateView):
    template_name = 'general/calculate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        material_calculator = MaterialCalculator()
        context["amount"] = material_calculator.calculate_material(product_type_id=1,
                                               mateirial_type_id=1,
                                               produced_product_amount=1,
                                               param_1=1,
                                               param_2=1)
        return context
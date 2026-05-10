from django.views.generic import TemplateView


class CalculateMaterialView(TemplateView):
    template_name = 'general/calculate.html'
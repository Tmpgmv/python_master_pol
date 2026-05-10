from django.views.generic import ListView

from partner_products.models import PartnerProduct


class SaleHistoryView(ListView):
    model = PartnerProduct

    def get_queryset(self):
        qs = super().get_queryset().filter(partner__pk=self.kwargs["pk"])
        return qs
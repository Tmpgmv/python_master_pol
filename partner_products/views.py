from django.views.generic import ListView

from partner_products.models import PartnerProduct


class SaleHistoryView(ListView):
    model = PartnerProduct
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from partners.models import Partner


class PartnerCreateView(SuccessMessageMixin,
                        CreateView):
    model = Partner
    fields = "__all__"
    success_url = reverse_lazy("home")
    success_message = "Партнер добавлен."


class PartnerUpdateView(SuccessMessageMixin,
                        UpdateView):
    model = Partner
    fields = "__all__"
    success_url = reverse_lazy("home")
    success_message = "Партнер обновлен."
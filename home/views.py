from django.views.generic import ListView  # PREP

from partners.models import Partner


class HomeView(ListView):  # PREP
    """
    PREP
    Редактировать данный файл по необходимости.
    При подготовке заготовки проекта надо
    было вывести на экран какой-то шаблон.
    Реальная задача может сильно отличаться.
    """

    template_name = "home/home.html"  # PREP
    model = Partner
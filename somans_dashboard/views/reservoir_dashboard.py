from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView


class ReservoirDashboardView(SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/database/reservoir_dashboard.html"

    def get_context_data(self, **kwargs):
        menu_category = 'database'
        context = super().get_context_data(**kwargs)
        context.update(
            menu_category=menu_category,
        )
        return context
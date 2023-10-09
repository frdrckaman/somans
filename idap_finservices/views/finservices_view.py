from idap_finservices.mixin import FinServicesAdmin
from somans_dashboard.view_mixins import IdapLoginMixin


class FinServiceDashboardView(IdapLoginMixin, FinServicesAdmin):
    template_name = f"idap_finservices/bootstrap/finservices.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

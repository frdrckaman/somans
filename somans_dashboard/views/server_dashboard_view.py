from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView


class ServerDashboardView(SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/server.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)


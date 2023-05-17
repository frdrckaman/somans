import json

from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView


class ServerDashboardView(SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/server.html"

    def get_context_data(self, **kwargs):
        menu_category = 'servers'
        context = super().get_context_data(**kwargs)
        svr_data = json.dumps(self.server_list)
        context.update(
            menu_category=menu_category,
            svr_data=svr_data
        )
        return context

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)


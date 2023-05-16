import json

from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView


class ListOfServerView(SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/list_of_server.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ls_svr_data = json.dumps(self.get_server_all)
        context.update(
            ls_svr_data=ls_svr_data
        )
        return context

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)


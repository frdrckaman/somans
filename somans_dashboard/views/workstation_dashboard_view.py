import json

from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView


class WorkstationDashboardView(SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/workstation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.new_workstation_software_list)
        wks_data = json.dumps(self.workstation_list)
        context.update(
            wks_data=wks_data
        )
        return context

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

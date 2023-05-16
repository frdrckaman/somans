import json

from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView


class NewWorkstationSoftwareView(SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/new-software-workstation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        nw_wks_sft_data = json.dumps(self.new_workstation_software_list)
        context.update(
            nw_wks_sft_data=nw_wks_sft_data
        )
        return context

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

import json

from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView


class NewWorkstationSoftwareView(SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/new-software-workstation.html"

    def get_context_data(self, **kwargs):
        menu_category = 'workstations'
        context = super().get_context_data(**kwargs)
        nw_wks_sft_data_ = json.dumps(self.new_sft_workstation(context.get("app_name")))
        nw_wks_sft_data = json.dumps(nw_wks_sft_data_)
        context.update(
            menu_category=menu_category,
            nw_wks_sft_data=nw_wks_sft_data
        )
        return context

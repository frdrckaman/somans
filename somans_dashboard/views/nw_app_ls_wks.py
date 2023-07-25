import json

from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView


class NewAppListWorkstationView(SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/nw_app_ls_wks.html"

    def get_context_data(self, **kwargs):
        menu_category = 'workstations'
        context = super().get_context_data(**kwargs)
        # nw_app_wks_ls = json.dumps(self.new_software_workstation_app)
        nw_app_wks_ls = json.dumps(self.new_software_workstation_app_nw)
        context.update(
            menu_category=menu_category,
            nw_app_wks_ls=nw_app_wks_ls
        )
        return context


import json

from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView


class WorkstationInstalledVsListView(SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/workstation_installed_vs_list.html"

    def get_context_data(self, **kwargs):
        menu_category = 'workstations'
        context = super().get_context_data(**kwargs)
        wks_inst_ls = json.dumps(self.software_inst_ls_nt_ls_workstation_dt)
        context.update(
            menu_category=menu_category,
            wks_inst_ls=wks_inst_ls,
        )
        return context


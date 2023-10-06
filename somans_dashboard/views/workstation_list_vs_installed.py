import json

from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView, IdapLoginMixin


class WorkstationListVsInstalledView(IdapLoginMixin, SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/workstation_list_vs_installed.html"

    def get_context_data(self, **kwargs):
        menu_category = 'workstations'
        context = super().get_context_data(**kwargs)
        wks_ls_inst = json.dumps(self.get_list_vs_workstation_installed_software)
        wks_ls_nt_inst = json.dumps(self.software_ls_nt_inst_workstation_dt)
        context.update(
            menu_category=menu_category,
            wks_ls_inst=wks_ls_inst,
            wks_ls_nt_inst=wks_ls_nt_inst,
        )
        return context


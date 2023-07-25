import json

from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView


class ServerInstalledVsListView(SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/server_installed_vs_list.html"

    def get_context_data(self, **kwargs):
        menu_category = 'servers'
        context = super().get_context_data(**kwargs)
        svr_inst_ls = json.dumps(self.software_inst_ls_nt_ls_server_dt)
        context.update(
            menu_category=menu_category,
            svr_inst_ls=svr_inst_ls,
        )
        return context


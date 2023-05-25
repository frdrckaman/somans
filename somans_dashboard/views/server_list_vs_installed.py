import json

from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView


class ServerListVsInstalledView(SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/server_list_vs_installed.html"

    def get_context_data(self, **kwargs):
        menu_category = 'servers'
        context = super().get_context_data(**kwargs)
        svr_ls_inst = json.dumps(self.get_list_vs_server_installed_software)
        svr_ls_nt_inst = json.dumps(self.software_ls_nt_inst_server_dt)
        context.update(
            menu_category=menu_category,
            svr_ls_inst=svr_ls_inst,
            svr_ls_nt_inst=svr_ls_nt_inst,
        )
        return context

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)


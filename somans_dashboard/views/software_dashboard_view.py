from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView

from somans_dashboard.view_mixins import SoftwareListboardView


class SoftwareDashboardView(SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/software.html"

    def get_context_data(self, **kwargs):
        menu_category = 'software'
        context = super().get_context_data(**kwargs)
        context.update(
            menu_category=menu_category,
            no_rm_sft_svr=self.no_removed_sft_server,
            no_nw_sft_svr=self.no_new_sft_server,
            no_removed_sft_wks=self.no_removed_sft_workstation,
            no_nw_sft_wks=self.no_new_sft_workstation,
            software_ls_nt_inst_server=len(self.software_ls_nt_inst_server_dt),
            software_ls_nt_inst_workstation=len(self.software_ls_nt_inst_workstation_dt),
            software_inst_ls_nt_ls_server=len(self.software_inst_ls_nt_ls_server_dt),
            software_inst_ls_nt_ls_workstation=len(self.software_inst_ls_nt_ls_workstation_dt),
        )
        return context

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)


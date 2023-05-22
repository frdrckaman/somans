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
        print(self.no_new_sft_server)
        context.update(
            menu_category=menu_category,
            no_rm_sft_svr=self.no_removed_sft_server,
            no_nw_sft_svr=self.no_new_sft_server,
            no_removed_sft_wks=self.no_removed_sft_workstation,
            no_nw_sft_wks=self.no_new_sft_workstation,
        )
        return context

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)


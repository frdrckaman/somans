import json

from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView


class InstalledSoftwareView(SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/software_list.html"

    def get_context_data(self, **kwargs):
        menu_category = 'software'
        context = super().get_context_data(**kwargs)
        app_svr_wks_ls = json.dumps(self.get_software_inst_svr_wks)
        context.update(
            menu_category=menu_category,
            app_svr_wks_ls=app_svr_wks_ls
        )
        return context


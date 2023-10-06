import json

from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView, IdapLoginMixin


class ServerNotManageSccm(IdapLoginMixin, SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/svr_not_manage_sccm.html"

    def get_context_data(self, **kwargs):
        menu_category = 'servers'
        context = super().get_context_data(**kwargs)
        svr_not_manage_sccm = json.dumps(self.svr_not_manage_sccm)
        context.update(
            menu_category=menu_category,
            svr_not_manage_sccm=svr_not_manage_sccm,
        )
        return context


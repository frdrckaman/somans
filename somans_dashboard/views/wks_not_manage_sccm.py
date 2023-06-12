import json

from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView


class WorkstationNotManageSccm(SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/wks_not_manage_sccm.html"

    def get_context_data(self, **kwargs):
        menu_category = 'workstations'
        context = super().get_context_data(**kwargs)
        wks_not_manage_sccm = json.dumps(self.wks_not_manage_sccm)
        context.update(
            menu_category=menu_category,
            wks_not_manage_sccm=wks_not_manage_sccm
        )
        return context

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)


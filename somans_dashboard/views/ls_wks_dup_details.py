import json

from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView


class ListWorkstationDuplicateDetailsView(SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/ls_wks_dup_details.html"

    def get_context_data(self, **kwargs):
        menu_category = 'workstations'
        context = super().get_context_data(**kwargs)
        ls_wks_dup_dtl_ = self.get_workstation_duplicate(context.get("server_name"))
        ls_wks_dup_dtl = json.dumps(ls_wks_dup_dtl_)
        context.update(
            menu_category=menu_category,
            ls_wks_dup_dtl=ls_wks_dup_dtl
        )
        return context

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)


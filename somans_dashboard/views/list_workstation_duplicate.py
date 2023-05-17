import json

from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView


class ListOfWorkstationDuplicateView(SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/list_workstation_duplicate.html"

    def get_context_data(self, **kwargs):
        menu_category = 'workstations'
        context = super().get_context_data(**kwargs)
        ls_wks_dup = json.dumps(self.get_duplicate_workstation_list)
        context.update(
            menu_category=menu_category,
            ls_wks_dup=ls_wks_dup
        )
        return context

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)


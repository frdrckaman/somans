import json

from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView, IdapLoginMixin


class ListOfWorkstationView(IdapLoginMixin, SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/list_of_workstation.html"

    def get_context_data(self, **kwargs):
        menu_category = 'workstations'
        context = super().get_context_data(**kwargs)
        ls_wks_data = json.dumps(self.get_workstation_all)
        context.update(
            menu_category=menu_category,
            ls_wks_data=ls_wks_data
        )
        return context


import json

from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView


class WorkstationDashboardView(SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/workstation.html"

    def get_context_data(self, **kwargs):
        menu_category = 'workstations'
        context = super().get_context_data(**kwargs)
        wks_data = json.dumps(self.workstation_list)
        context.update(
            menu_category=menu_category,
            wks_data=wks_data,
        )
        return context

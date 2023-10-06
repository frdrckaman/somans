import json

from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView, IdapLoginMixin


class RemovedSoftwareWorkstationView(IdapLoginMixin, SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/removed_sft_wks.html"

    def get_context_data(self, **kwargs):
        menu_category = 'workstations'
        context = super().get_context_data(**kwargs)
        rm_sft_wks = json.dumps(self.removed_sft_workstation)
        context.update(
            menu_category=menu_category,
            rm_sft_wks=rm_sft_wks,
        )
        return context


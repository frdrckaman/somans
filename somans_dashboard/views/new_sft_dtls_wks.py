import json

import pandas as pd
from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView


class NewSoftwareWorkstationDetailsView(SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/new_sft_dtls_wks.html"

    def get_context_data(self, **kwargs):
        menu_category = 'workstations'
        context = super().get_context_data(**kwargs)
        new_sft_workstation_dup = json.dumps(self.new_sft_workstation_dup)
        context.update(
            menu_category=menu_category,
            new_sft_workstation_dup=new_sft_workstation_dup,
        )
        return context

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)


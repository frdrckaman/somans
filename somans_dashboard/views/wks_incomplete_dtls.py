import json

from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView, IdapLoginMixin


class IncompleteWorkstationDetailsView(IdapLoginMixin, SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/wks_incomplete_dtls.html"

    def get_context_data(self, **kwargs):
        menu_category = 'workstations'
        context = super().get_context_data(**kwargs)
        wks_inc_dtls = json.dumps(self.get_wks_incomplete_details)
        context.update(
            menu_category=menu_category,
            wks_inc_dtls=wks_inc_dtls,
        )
        return context


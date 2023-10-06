import json

from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView, IdapLoginMixin


class IncompleteServerDetailsView(IdapLoginMixin, SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/svr_incomplete_dtls.html"

    def get_context_data(self, **kwargs):
        menu_category = 'servers'
        context = super().get_context_data(**kwargs)
        svr_inc_dtls = json.dumps(self.get_svr_incomplete_details)
        context.update(
            menu_category=menu_category,
            svr_inc_dtls=svr_inc_dtls,
        )
        return context


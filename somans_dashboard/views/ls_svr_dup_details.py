import json

from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView, IdapLoginMixin


class ListServerDuplicateDetailsView(IdapLoginMixin, SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/ls_svr_dup_details.html"

    def get_context_data(self, **kwargs):
        menu_category = 'servers'
        context = super().get_context_data(**kwargs)
        ls_svr_dup_dtl_ = self.get_server_duplicate(context.get("server_name"))
        ls_svr_dup_dtl = json.dumps(ls_svr_dup_dtl_)
        context.update(
            menu_category=menu_category,
            ls_svr_dup_dtl=ls_svr_dup_dtl
        )
        return context


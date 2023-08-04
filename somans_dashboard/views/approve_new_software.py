import json

from django.views.generic.base import TemplateView

from somans_dashboard.models import ApproveSoftware
from somans_dashboard.view_mixins import SoftwareListboardView


class ApproveSoftwareSvrWksView(SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/approve_new_software.html"

    def get_context_data(self, **kwargs):
        menu_category = 'Approval'
        context = super().get_context_data(**kwargs)
        uid = ApproveSoftware.objects.get(product_name=context.get("app_name"))
        svr_wks_sft_app = json.dumps(self.get_server_workstation_app(context.get("app_name")))
        context.update(
            app_status=uid.status,
            menu_category=menu_category,
            svr_wks_sft_app=svr_wks_sft_app,
        )
        return context


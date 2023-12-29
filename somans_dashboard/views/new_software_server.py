import json

from django.views.generic.base import TemplateView

from somans_dashboard.models import ApproveSoftware
from somans_dashboard.view_mixins import SoftwareListboardView, IdapLoginMixin


class NewServerSoftwareView(IdapLoginMixin, SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/new-software-server.html"

    def get_context_data(self, **kwargs):
        menu_category = 'servers'
        context = super().get_context_data(**kwargs)
        nw_svr_sft_data_ = json.dumps(self.new_sft_server(context.get("app_name")))
        nw_svr_sft_data = json.dumps(nw_svr_sft_data_)
        uid = ApproveSoftware.objects.filter(product_name=context.get("app_name"))
        app_status = list(uid.values())[0]['status'] if uid else None
        context.update(
            app_status=app_status,
            menu_category=menu_category,
            nw_svr_sft_data=nw_svr_sft_data
        )
        return context


import json

from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView, IdapLoginMixin


class ServerDetailsView(IdapLoginMixin, SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/server-details.html"

    def get_context_data(self, **kwargs):
        menu_category = 'servers'
        context = super().get_context_data(**kwargs)
        svr_details = self.get_server(context.get("server_name"))[0] if self.get_server(context.get("server_name")) else None
        svr_sft_all = self.get_server_app(context.get("server_name"))
        svr_sft_one = svr_sft_all[0]
        svr_sft_ = self.get_server_new(context.get("server_name"))
        svr_sft_info = json.dumps(svr_sft_)
        context.update(
            menu_category=menu_category,
            svr_details=svr_details,
            svr_sft_all=svr_sft_all,
            svr_sft_one=svr_sft_one,
            no_sft=len(svr_sft_all),
            svr_sft_info=svr_sft_info,
        )
        return context


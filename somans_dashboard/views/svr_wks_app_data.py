import json

from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView, IdapLoginMixin


class ServerSoftwareAppView(IdapLoginMixin, SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/svr_wks_app_data.html"

    def get_context_data(self, **kwargs):
        menu_category = 'software'
        context = super().get_context_data(**kwargs)
        svr_wks_sft_data_ = json.dumps(self.svr_wks_list_data(context.get("app_name")))
        svr_wks_sft_data = json.dumps(svr_wks_sft_data_)
        context.update(
            menu_category=menu_category,
            svr_wks_sft_data=svr_wks_sft_data
        )
        return context


import json

import pandas as pd
from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView


class NewServerSoftwareView(SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/new-software-server.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        nw_svr_sft_data = json.dumps(self.new_server_software_list)
        context.update(
            nw_svr_sft_data=nw_svr_sft_data
        )
        return context

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)


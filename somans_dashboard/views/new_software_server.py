import json

import pandas as pd
from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView


class NewServerSoftwareView(SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/new-software-server.html"

    def get_context_data(self, **kwargs):
        menu_category = 'servers'
        context = super().get_context_data(**kwargs)
        nw_svr_sft_data_ = json.dumps(self.new_sft_server(context.get("app_name")))
        nw_svr_sft_data = json.dumps(nw_svr_sft_data_)
        context.update(
            menu_category=menu_category,
            nw_svr_sft_data=nw_svr_sft_data
        )
        return context

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)


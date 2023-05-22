import json

import pandas as pd
from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView


class NewAppListServerView(SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/nw_app_ls_svr.html"

    def get_context_data(self, **kwargs):
        menu_category = 'servers'
        context = super().get_context_data(**kwargs)
        nw_app_svr_ls = json.dumps(self.new_software_server_app)
        context.update(
            menu_category=menu_category,
            nw_app_svr_ls=nw_app_svr_ls
        )
        return context

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)


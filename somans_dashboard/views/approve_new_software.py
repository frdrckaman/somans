import json
import pandas as pd

from django.views.generic.base import TemplateView
from django.conf import settings
from somans_dashboard.models import ApproveSoftware
from somans_dashboard.view_mixins import SoftwareListboardView, IdapLoginMixin


class ApproveSoftwareSvrWksView(IdapLoginMixin, SoftwareListboardView, TemplateView):
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

    def get_server_workstation_app(self, name):
        df1 = pd.read_sql(
            f"select * from (select * from {settings.SOMANS_SFTWR_SVRS}  union select * from {settings.SOMANS_SFTWR_WKS}) a "
            f"left join (select * from {settings.SOMANS_LS_OF_WKS} union select a.*, null os_build_version, null user_email from {settings.SOMANS_LS_OF_SVRS} a) b "
            f"on a.computer_name = b.computer_name where a.product_name = '{name}'",
            settings.SOMANS_ENGINE)
        # df11 = df1.drop_duplicates(['computer_name'])
        return df1.to_dict('records')


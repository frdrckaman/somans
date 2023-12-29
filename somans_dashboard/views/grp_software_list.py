import json
import pandas as pd

from django.conf import settings
from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView, IdapLoginMixin


class GroupSoftwareList(IdapLoginMixin, TemplateView):
    template_name = f"somans_dashboard/bootstrap/grp_software_list.html"

    def get_context_data(self, **kwargs):
        menu_category = 'software'
        context = super().get_context_data(**kwargs)
        group_software_list = json.dumps(self.group_software_list)
        context.update(
            menu_category=menu_category,
            group_software_list=group_software_list
        )
        return context

    @property
    def group_software_list(self):
        df = pd.read_sql(f"select * from {settings.SOMANS_GRP_SFTWR}", settings.SOMANS_ENGINE)
        return df.to_dict('records')


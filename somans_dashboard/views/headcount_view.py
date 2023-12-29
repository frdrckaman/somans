import json
import pandas as pd
from django.conf import settings
from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView, IdapLoginMixin


class HeadcountView(IdapLoginMixin, SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/headcount.html"

    def get_context_data(self, **kwargs):
        menu_category = 'software'
        context = super().get_context_data(**kwargs)
        head_data = json.dumps(self.headcount_data)
        context.update(
            menu_category=menu_category,
            head_data=head_data
        )
        return context

    @property
    def headcount_data(self):
        df2 = pd.read_sql(f'select * from {settings.SOMANS_HEADCOUNT}', settings.SOMANS_ENGINE)
        df22 = df2.drop_duplicates(['personnel_number'])
        return df22.to_dict('records')


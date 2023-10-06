import json

from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView, IdapLoginMixin


class RemovedSoftwareServerView(IdapLoginMixin, SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/removed_sft_svr.html"

    def get_context_data(self, **kwargs):
        menu_category = 'servers'
        context = super().get_context_data(**kwargs)
        rm_sft_svr = json.dumps(self.removed_sft_server)
        context.update(
            menu_category=menu_category,
            rm_sft_svr=rm_sft_svr,
        )
        return context


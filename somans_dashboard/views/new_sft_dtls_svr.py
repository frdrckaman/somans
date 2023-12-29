import json

from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView, IdapLoginMixin


class NewSoftwareServerDetailsView(IdapLoginMixin, SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/new_sft_dtls_svr.html"

    def get_context_data(self, **kwargs):
        menu_category = 'servers'
        context = super().get_context_data(**kwargs)
        new_sft_server_dup = json.dumps(self.new_sft_server_dup)
        context.update(
            menu_category=menu_category,
            new_sft_server_dup=new_sft_server_dup,
        )
        return context


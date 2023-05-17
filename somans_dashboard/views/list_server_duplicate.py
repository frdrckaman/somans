import json

from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView


class ListOfServerDuplicateView(SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/list_server_duplicate.html"

    def get_context_data(self, **kwargs):
        menu_category = 'servers'
        context = super().get_context_data(**kwargs)
        ls_svr_dup = json.dumps(self.get_duplicate_server_list)
        context.update(
            menu_category=menu_category,
            ls_svr_dup=ls_svr_dup
        )
        return context

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)


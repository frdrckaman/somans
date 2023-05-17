import json

from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView


class HeadcountView(SoftwareListboardView, TemplateView):
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

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)


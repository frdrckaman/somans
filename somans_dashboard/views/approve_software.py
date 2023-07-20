import json

from django.core.serializers.json import DjangoJSONEncoder
from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView
from somans_dashboard.models import ApproveSoftware


class ApproveSoftwareView(SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/approve_software.html"

    def get_context_data(self, **kwargs):
        menu_category = 'Approval'
        queryset = ApproveSoftware.objects.filter(status=0).values()
        context = super().get_context_data(**kwargs)
        approval_list = json.dumps(list(queryset), cls=DjangoJSONEncoder)
        context.update(
            menu_category=menu_category,
            approval_list=approval_list,
        )
        return context

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)


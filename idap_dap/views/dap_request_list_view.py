import json

from django.core.serializers.json import DjangoJSONEncoder
from django.views.generic.base import TemplateView
from idap_dap.models import DataCenterAccessRequest


class DataCenterAccessRequestListView(TemplateView):
    template_name = f"idap_dap/bootstrap/dca_request_list.html"

    def get_context_data(self, **kwargs):
        menu_category = ''
        context = super().get_context_data(**kwargs)
        dca_request_list = DataCenterAccessRequest.objects.all().values()
        dca_request = json.dumps(list(dca_request_list), cls=DjangoJSONEncoder)
        context.update(
            menu_category=menu_category,
            dca_request=dca_request
        )
        return context

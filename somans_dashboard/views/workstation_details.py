import json

from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import SoftwareListboardView


class WorkstationDetailsView(SoftwareListboardView, TemplateView):
    template_name = f"somans_dashboard/bootstrap/workstation-details.html"

    def get_context_data(self, **kwargs):
        menu_category = 'workstations'
        context = super().get_context_data(**kwargs)
        wks_details = self.get_workstation(context.get("server_name"))[0]
        wks_sft_all = self.get_workstation_app(context.get("server_name"))
        wks_sft_one = wks_sft_all[0]
        wks_sft_ = self.get_workstation_new(context.get("server_name"))
        wks_sft_info = json.dumps(wks_sft_)
        context.update(
            menu_category=menu_category,
            wks_details=wks_details,
            wks_sft_all=wks_sft_all,
            wks_sft_one=wks_sft_one,
            no_sft=len(wks_sft_all),
            wks_sft_info=wks_sft_info,
        )
        return context

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)


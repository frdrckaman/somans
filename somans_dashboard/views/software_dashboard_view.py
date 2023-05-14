from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
import pandas as pd


class SoftwareDashboardView(TemplateView):
    template_name = f"somans_dashboard/bootstrap/software.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        frd = pd.read_sql('select * from headcount', settings.SOMANS_ENGINE)
        print(frd)
        # site_profile = Site.objects.get_current()
        # context.update(
        #     installed_apps=settings.INSTALLED_APPS,
        #     # s_id=site_profile.id
        # )
        return context

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)


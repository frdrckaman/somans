from django.views.generic.base import TemplateView
from somans_dashboard.view_mixins import IdapLoginMixin


class OracleDbDailyChecks(IdapLoginMixin, TemplateView):
    template_name = f"idap_database/bootstrap/oracle_daily_checks.html"

    def get_context_data(self, **kwargs):
        menu_category = 'database'
        context = super().get_context_data(**kwargs)
        context.update(
            menu_category=menu_category,
        )
        return context
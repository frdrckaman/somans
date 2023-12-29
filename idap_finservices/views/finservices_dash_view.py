from idap_finservices.mixin import FinServicesAdmin


class FinServiceDashView(FinServicesAdmin):
    template_name = f"idap_finservices/bootstrap/finservice_dash.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

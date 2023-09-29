from django.views.generic import TemplateView


class DataCenterAccessRequestView(TemplateView):
    template_name = f"idap_dap/bootstrap/dap_request.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
        )
        return context

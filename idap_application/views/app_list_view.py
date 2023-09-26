from django.views.generic import TemplateView


class AppListView(TemplateView):
    template_name = f"idap_application/bootstrap/app_links.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
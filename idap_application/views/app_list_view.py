from django.views.generic import TemplateView

from idap_application.models import ApplicationLinks


class AppListView(TemplateView):
    template_name = f"idap_application/bootstrap/app_links.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        apps = ApplicationLinks.objects.all().order_by('app_name')
        context.update(
            apps=apps,
        )
        return context

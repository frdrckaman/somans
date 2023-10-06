from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView

from somans_dashboard.view_mixins import IdapLoginMixin


class WelcomeView(IdapLoginMixin, TemplateView):
    template_name = f"somans_dashboard/bootstrap/welcome.html"

    def get_context_data(self, **kwargs):
        menu_category = ''
        context = super().get_context_data(**kwargs)
        context.update()
        return context

    @method_decorator(login_required(login_url='somans_auth:login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
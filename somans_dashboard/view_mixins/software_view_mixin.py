from django.apps import apps as django_apps
from django.urls import reverse


class SoftwareListboardView:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    @property
    def get_server_installed_software_data(self):
        pass

    @property
    def get_workstation_installed_software_data(self):
        pass

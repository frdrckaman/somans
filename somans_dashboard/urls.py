from django.contrib import admin
from django.urls import path

from somans_dashboard.views import WorkstationDashboardView, NewWorkstationSoftwareView, \
    NewServerSoftwareView
from somans_dashboard.views.server_dashboard_view import ServerDashboardView
from somans_dashboard.views.software_dashboard_view import SoftwareDashboardView

app_name = "somans_dashboard"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("server/", ServerDashboardView.as_view(), name="server"),
    path("workstation/", WorkstationDashboardView.as_view(), name="workstation"),
    path("new-workstation-app/", NewWorkstationSoftwareView.as_view(), name="new-workstation-app"),
    path("new-server-app/", NewServerSoftwareView.as_view(), name="new-server-app"),
    path("", SoftwareDashboardView.as_view(), name="software-home"),
]
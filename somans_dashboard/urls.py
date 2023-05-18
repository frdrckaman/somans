from django.contrib import admin
from django.urls import path

from somans_dashboard.views import WorkstationDashboardView, NewWorkstationSoftwareView, \
    NewServerSoftwareView, ServerDetailsView, WorkstationDetailsView, ListOfServerView, \
    ListOfWorkstationView, ServerListVsInstalledView, ListOfWorkstationDuplicateView, \
    ListOfServerDuplicateView, ListWorkstationDuplicateDetailsView, ListServerDuplicateDetailsView, HeadcountView
from somans_dashboard.views.server_dashboard_view import ServerDashboardView
from somans_dashboard.views.software_dashboard_view import SoftwareDashboardView
from somans_dashboard.views.workstation_list_vs_installed import WorkstationListVsInstalledView

app_name = "somans_dashboard"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("server/", ServerDashboardView.as_view(), name="server"),
    path("workstation/", WorkstationDashboardView.as_view(), name="workstation"),
    path("new-workstation-app/", NewWorkstationSoftwareView.as_view(), name="new-workstation-app"),
    path("new-server-app/", NewServerSoftwareView.as_view(), name="new-server-app"),
    path("server/<server_name>", ServerDetailsView.as_view(), name="server-details"),
    path("workstation/<server_name>", WorkstationDetailsView.as_view(), name="workstation-details"),
    path("list-server/", ListOfServerView.as_view(), name="list-server"),
    path("list-workstation/", ListOfWorkstationView.as_view(), name="list-workstation"),
    path("svr-ls-inst/", ServerListVsInstalledView.as_view(), name="svr-ls-inst"),
    path("wks-ls-inst/", WorkstationListVsInstalledView.as_view(), name="wks-ls-inst"),
    path("wks-ls-dup/", ListOfWorkstationDuplicateView.as_view(), name="wks-ls-dup"),
    path("svr-ls-dup/", ListOfServerDuplicateView.as_view(), name="svr-ls-dup"),
    path("wks-ls-dup/<server_name>", ListWorkstationDuplicateDetailsView.as_view(), name="wks-ls-dup-dtl"),
    path("svr-ls-dup/<server_name>", ListServerDuplicateDetailsView.as_view(), name="svr-ls-dup-dtl"),
    path("headcount/", HeadcountView.as_view(), name="headcount"),
    path("", SoftwareDashboardView.as_view(), name="software-home"),
]
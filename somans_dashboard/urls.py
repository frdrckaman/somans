from django.contrib import admin
from django.urls import path

from somans import settings
from somans_dashboard.views import WorkstationDashboardView, NewWorkstationSoftwareView, \
    NewServerSoftwareView, ServerDetailsView, WorkstationDetailsView, ListOfServerView, \
    ListOfWorkstationView, ServerListVsInstalledView, ListOfWorkstationDuplicateView, \
    ListOfServerDuplicateView, ListWorkstationDuplicateDetailsView, \
    ListServerDuplicateDetailsView, HeadcountView, RemovedSoftwareServerView, \
    RemovedSoftwareWorkstationView, NewAppListServerView, NewAppListWorkstationView, \
    ServerInstalledVsListView, \
    WorkstationInstalledVsListView, InstalledSoftwareView, IncompleteServerDetailsView, \
    IncompleteWorkstationDetailsView, ServerSoftwareAppView, NewSoftwareServerDetailsView, \
    NewSoftwareWorkstationDetailsView, ServerNotManageSccm, WorkstationNotManageSccm, GroupSoftwareList, \
    ApproveSoftwareView
from somans_dashboard.views.request_software_approval import send_approval_request, approve_request
from somans_dashboard.views.server_dashboard_view import ServerDashboardView
from somans_dashboard.views.software_dashboard_view import SoftwareDashboardView
from somans_dashboard.views.workstation_list_vs_installed import WorkstationListVsInstalledView

app_name = "somans_dashboard"

admin.site.site_header = settings.APP_NAME

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
    path("svr-inst-ls/", ServerInstalledVsListView.as_view(), name="svr-inst-ls"),
    path("wks-ls-inst/", WorkstationListVsInstalledView.as_view(), name="wks-ls-inst"),
    path("wks-inst-ls/", WorkstationInstalledVsListView.as_view(), name="wks-inst-ls"),
    path("wks-ls-dup/", ListOfWorkstationDuplicateView.as_view(), name="wks-ls-dup"),
    path("svr-ls-dup/", ListOfServerDuplicateView.as_view(), name="svr-ls-dup"),
    path("wks-ls-dup/<server_name>", ListWorkstationDuplicateDetailsView.as_view(), name="wks-ls-dup-dtl"),
    path("svr-ls-dup/<server_name>", ListServerDuplicateDetailsView.as_view(), name="svr-ls-dup-dtl"),
    path("headcount/", HeadcountView.as_view(), name="headcount"),
    path("rm-sft-svr/", RemovedSoftwareServerView.as_view(), name="rm-sft-svr"),
    path("rm-sft-wks/", RemovedSoftwareWorkstationView.as_view(), name="rm-sft-wks"),
    path("nw-app-ls-svr/", NewAppListServerView.as_view(), name="nw-app-ls-svr"),
    path("nw-app-ls-svr/<app_name>", NewServerSoftwareView.as_view(), name="nw-app-dtls-svr"),
    path("nw-app-ls-wks/", NewAppListWorkstationView.as_view(), name="nw-app-ls-wks"),
    path("nw-app-ls-wks/<app_name>", NewWorkstationSoftwareView.as_view(), name="nw-app-dtls-wks"),
    path("app-svr-wks/", InstalledSoftwareView.as_view(), name="app-svr-wks"),
    path("svr-inc-dtls/", IncompleteServerDetailsView.as_view(), name="svr-inc-dtls"),
    path("wks-inc-dtls/", IncompleteWorkstationDetailsView.as_view(), name="wks-inc-dtls"),
    path("app-svr-wks/<app_name>", ServerSoftwareAppView.as_view(), name="svr-wks-app-data"),
    path("new-sft-dtls-svr/", NewSoftwareServerDetailsView.as_view(), name="new-sft-dtls-svr"),
    path("new-sft-dtls-wks/", NewSoftwareWorkstationDetailsView.as_view(), name="new-sft-dtls-wks"),
    path("svr-not-manage-sccm/", ServerNotManageSccm.as_view(), name="svr-not-manage-sccm"),
    path("wks-not-manage-sccm/", WorkstationNotManageSccm.as_view(), name="wks-not-manage-sccm"),
    path("grp-software-list/", GroupSoftwareList.as_view(), name="grp-software-list"),

    path("ap-nw-app-ls-svr/", send_approval_request, name="ap-nw-app-ls-svr"),
    path("ap-nw-app-ls-wks/", send_approval_request, name="ap-nw-app-ls-wks"),

    path("approve-sft-req/", ApproveSoftwareView.as_view(), name="approve-sft-req"),

    path("approve-sft-req-svr/<app_name>", NewServerSoftwareView.as_view(), name="approve-req-dtls-svr"),
    path("approve-sft-req-wks/<app_name>", NewWorkstationSoftwareView.as_view(), name="approve-req-dtls-wks"),

    path("aprv-rqst-sft/", approve_request, name="aprv-rqst-sft"),
    path("approve-sft-req/<app_name>", NewWorkstationSoftwareView.as_view(), name="approve-req-dtls-wks"),
    path("", SoftwareDashboardView.as_view(), name="software-home"),
    # path("", SoftwareDashboardView.as_view(), name="software-home"),
]
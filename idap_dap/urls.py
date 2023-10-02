from django.urls import path

from idap_dap.views import DataCenterAccessRequestView, DataCenterAccessApprovalView, DataCenterAccessRequestListView
from idap_dap.views.dap_approval_view import dc_approve_request
from idap_dap.views.dap_request_view import dc_access_request

app_name = "idap-dap"

urlpatterns = [
    path("da-request/", dc_access_request, name="da-request"),
    path("da-approval/", dc_approve_request, name="da-approval"),
    path("dap-request/", DataCenterAccessRequestView.as_view(), name="dap-request"),
    path("dap-approval/", DataCenterAccessApprovalView.as_view(), name="dap-approval"),
    path("dac-list/", DataCenterAccessRequestListView.as_view(), name="dac-list"),
]
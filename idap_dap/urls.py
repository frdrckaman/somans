from django.urls import path

from idap_dap.views import DataCenterAccessRequestView
from idap_dap.views.dap_request_view import dc_access_request

app_name = "idap-dap"

urlpatterns = [
    path("da-request/", dc_access_request, name="da-request"),
    path("dap-request/", DataCenterAccessRequestView.as_view(), name="dap-request"),
]
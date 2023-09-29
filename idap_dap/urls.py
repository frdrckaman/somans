from django.urls import path

from idap_dap.views import DataCenterAccessRequestView

app_name = "idap-dap"

urlpatterns = [
    path("", DataCenterAccessRequestView.as_view(), name="dap_request"),
]
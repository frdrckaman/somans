from django.urls import path

from idap_finservices.views import FinServiceDashboardView

app_name = "idap-finservices"

urlpatterns = [
    path("", FinServiceDashboardView.as_view(), name="finservices"),
]
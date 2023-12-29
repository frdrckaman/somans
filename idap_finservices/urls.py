from django.urls import path

from idap_finservices.views import FinServiceDashboardView, FinServiceDashView

app_name = "idap-finservices"

urlpatterns = [
    # path("", FinServiceDashboardView.as_view(), name="finservices"),
    path("finservicedash/", FinServiceDashView.as_view(), name="finservicedash"),
]
from django.urls import path

from idap_database.views import ReservoirDashboardView, OracleDbDailyChecks

app_name = "idap-database"

urlpatterns = [
    path("reservoir/", ReservoirDashboardView.as_view(), name="reservoir"),
    path("oralce-checks/", OracleDbDailyChecks.as_view(), name="oracle-checks"),
]
from django.urls import path

from idap_database.views import ReservoirDashboardView, OracleDbDailyChecks, OracleDbSync

app_name = "idap-database"

urlpatterns = [
    path("reservoir/", ReservoirDashboardView.as_view(), name="reservoir"),
    path("oralce-checks/", OracleDbDailyChecks.as_view(), name="oracle-checks"),
    path("oralce-sync/", OracleDbSync.as_view(), name="oracle-sync"),
]
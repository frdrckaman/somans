from django.urls import path

from idap_database.views import ReservoirDashboardView, OracleDbDailyChecks, OracleDbSync

app_name = "idap-pos"

# urlpatterns = [
#     path("add-merchant/", ReservoirDashboardView.as_view(), name="add-merchant"),
# ]
from django.contrib import admin
from django.urls import path

from somans_dashboard.views.software_dashboard_view import SoftwareDashboardView

app_name = "somans_dashboard"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", SoftwareDashboardView.as_view(), name="software-home"),
]
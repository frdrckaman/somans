from django.contrib import admin
from django.urls import path

from somans_dashboard.views.dashboard_view import HomeView

app_name = "somans_dashboard"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view(), name="home"),
]
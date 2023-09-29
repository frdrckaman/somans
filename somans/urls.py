from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("applications/", include("idap_application.urls")),
    path("dap/", include("idap_dap.urls")),
    path("finservices/", include("idap_finservices.urls")),
    path("database/", include("idap_database.urls")),
    path("software-home/", include("somans_dashboard.urls")),
    path("", include("somans_auth.urls"))
]

handler404 = "somans_dashboard.views.handle_not_found"
handler500 = "somans_dashboard.views.handle_server_error"

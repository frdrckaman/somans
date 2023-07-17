from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("software-home/", include("somans_dashboard.urls")),
    path("", include("somans_auth.urls"))
]

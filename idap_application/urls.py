from django.urls import path

from idap_application.views.app_list_view import AppListView

app_name = "idap-application"

urlpatterns = [
    path("", AppListView.as_view(), name="application_list"),
]
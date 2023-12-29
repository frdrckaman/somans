from django.urls import path

from somans_auth.views import LoginView, LogoutView

app_name = "somans_auth"

urlpatterns = [
    path('', LoginView.as_view(redirect_authenticated_user=True), name="login"),
    path('logout/', LogoutView.as_view(template_name="somans_auth/bootstrap/login.html"),
         name="logout",),
]

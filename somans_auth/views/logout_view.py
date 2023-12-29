from django.contrib.auth.views import LogoutView as BaseLogoutView


class LogoutView(BaseLogoutView):
    next_page = 'somans_auth:login'

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class IdapLoginMixin:
    @method_decorator(login_required(login_url='somans_auth:login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
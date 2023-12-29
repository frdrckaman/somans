from django.shortcuts import redirect
from django.urls import reverse

from somans_dashboard.models import AppTheme


def change_theme(request):
    usr = AppTheme.objects.filter(theme_user=request.user)
    if usr:
        AppTheme.objects.filter(theme_user=request.user).update(
            theme_name=request.GET.get("name"),
            theme_mode=request.GET.get("mode"),
        )
    else:
        AppTheme.objects.get_or_create(
            theme_name=request.GET.get("name"),
            theme_mode=request.GET.get("mode"),
            theme_user=request.user,
        )
    app_name = 'idap-finservices' if 'fins' in request.GET.get("next") else 'somans_dashboard'
    return redirect(reverse(f'{app_name}:{request.GET.get("next")}'))

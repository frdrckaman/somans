from django.shortcuts import redirect
from django.urls import reverse

from somans_dashboard.models import ApproveSoftware


def send_approval_request(request, url=None):
    if request.method == 'POST':
        ticket, created = ApproveSoftware.objects.get_or_create(
            product_name=request.POST.get("app_name"),
            devices_permitted=request.POST.get("devices_permitted"),
            reasons=request.POST.get("reasons")
        )
        if created:
            res = 'success'
            message = 'Request submitted successful'
        else:
            res = 'error'
            message = 'Error occurred while your request,please check your inputs and try again'
        notification = res + '&message=' + message
        url = "?response=".join([reverse('somans_dashboard:nw-app-ls-svr'), notification])
    return redirect(url)

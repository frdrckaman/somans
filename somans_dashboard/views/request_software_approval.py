import getpass
from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone

from somans_dashboard.models import ApproveSoftware


def send_approval_request(request, url=None):
    if request.method == 'POST':
        ticket, created = ApproveSoftware.objects.get_or_create(
            product_name=request.POST.get("app_name"),
            devices_permitted=request.POST.get("devices_permitted"),
            reasons=request.POST.get("reasons"),
            next_url_name=request.POST.get("next_url_name"),
        )
        if created:
            res = 'success'
            message = 'Request submitted successful'
        else:
            res = 'error'
            message = 'Error occurred while your request,please check your inputs and try again'
        notification = res + '&message=' + message
        url = "?response=".join([reverse(request.POST.get("nxt_request")), notification])
    return redirect(url)


def approve_request(request, url=None):
    if request.method == 'POST':
        ticket, created = ApproveSoftware.objects.update_or_create(
            approve=getpass.getuser(),
            approve_date=timezone.now,
            approve_datetime=timezone.now,
            status=request.POST.get("approve"),
            approve_review=request.POST.get("approve_review"),
            comment=request.POST.get("comment")
        )
        if created:
            res = 'success'
            message = 'Request Approved successful'
        else:
            res = 'error'
            message = 'Error occurred while approving this request,please check your inputs and try again'
        notification = res + '&message=' + message
        url = "?response=".join([reverse(request.POST.get("nxt_approval")), notification])
    return redirect(url)

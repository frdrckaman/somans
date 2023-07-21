import getpass
from datetime import datetime

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
        url = "?response=".join([reverse(f'somans_dashboard:{request.POST.get("next_url_name")}'), notification])
    return redirect(url)


def approve_request(request, url=None):
    if request.method == 'POST':
        try:
            ApproveSoftware.objects.filter(id=request.POST.get("id")).update(
                approve=getpass.getuser(),
                approve_date=datetime.today().strftime('%Y-%m-%d'),
                approve_datetime=timezone.now(),
                status=request.POST.get("approve"),
                approve_review=request.POST.get("approve_review"),
                comment=request.POST.get("comment"))
            res = 'success'
            message = 'Request Approved successful'

        except Exception as e:
            print(e)
            res = 'error'
            message = 'Error occurred while approving this request,please check your inputs and try again'

        notification = res + '&message=' + message
        url = "?response=".join([reverse('somans_dashboard:approve-sft-req'), notification])
    return redirect(url)

from datetime import datetime

from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.urls import reverse
from idap_dap.models import DataCenterAccessRequest


class DataCenterAccessRequestView(TemplateView):
    template_name = f"idap_dap/bootstrap/dap_request.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
        )
        return context


def dc_access_request(request, url=None):
    if request.method == 'POST':
        ticket, created = DataCenterAccessRequest.objects.get_or_create(
            location=request.POST.get("location"),
            visitor_name=request.POST.get("visitor_name"),
            visitor_org=request.POST.get("visitor_org"),
            visitor_phone=request.POST.get("visitor_phone"),
            visitor_email=request.POST.get("visitor_email"),
            visitor_address=request.POST.get("visitor_address"),
            start_date=datetime.strptime(request.POST.get("start_date"), '%d %b, %Y'),
            start_time=request.POST.get("start_time"),
            end_date=datetime.strptime(request.POST.get("end_date"), '%d %b, %Y'),
            end_time=request.POST.get("end_time"),
            reason=request.POST.get("reason"),
            requester=request.user,
        )
        if created:
            res = 'success'
            message = 'Request submitted successful'
        else:
            res = 'error'
            message = 'Error occurred while your request,please check your inputs and try again'
        notification = res + '&message=' + message
        url = "?response=".join([reverse(f'idap-dap:dap-request'), notification])
        print(url)
    return redirect(url)

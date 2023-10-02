from django.utils import timezone
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.urls import reverse
from idap_dap.models import DataCenterAccessRequest


class DataCenterAccessApprovalView(TemplateView):
    template_name = f"idap_dap/bootstrap/dap_approval.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        approvals = DataCenterAccessRequest.objects.filter(status=0)
        context.update(
            approvals=approvals,
        )
        return context


def dc_approve_request(request, url=None):
    if request.method == 'POST':
        try:
            print(request.POST.get("id"))
            DataCenterAccessRequest.objects.filter(id=request.POST.get("id")).update(
                approver=str(request.user),
                approval_date=timezone.now(),
                status=request.POST.get("approve"),
                approval_comment=request.POST.get("approval_comment"))
            res = 'success'
            message = 'Request Approved successful'

        except Exception as e:
            res = 'error'
            message = 'Error occurred while approving this request,please check your inputs and try again'

        notification = res + '&message=' + message
        url = "?response=".join([reverse('idap-dap:dap-approval'), notification])
    return redirect(url)

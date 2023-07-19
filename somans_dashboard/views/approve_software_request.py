from django.shortcuts import redirect
from somans_dashboard.models import ApproveSoftware


def send_approval_request(request):
    if request.method == 'POST':
        print(request.POST.get("app_name"))
        print(request.POST.get("devices_permitted"))
        print(request.POST.get("reasons"))
        # ticket, created = ApproveSoftware.objects.get_or_create(
        #     product_name=request.POST.get("app_name"),
        #     devices_permitted=request.POST.get("devices_permitted"),
        #     reasons=request.POST.get("reasons")
        # )
        # if created:
        #     print('Oooooooooooooooooooooooooooook')
        # else:
        #     print('Nooooooooooooooooooooooooooooo')
    return redirect('somans_dashboard:nw-app-ls-svr')
